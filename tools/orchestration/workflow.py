"""LangGraph workflow for the Tiny Studio vertical-slice pipeline.

Nodes map to skill stage boundaries. State is shared via SliceState.
Paid generation nodes only execute after plan_approved is True.

Usage:
    python tools/orchestration/workflow.py [--project-root PATH]

If LangGraph is not installed, the script exits with an install hint.
The manual skill sequence in /vertical-slice is identical to this graph.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    from langgraph.graph import END, StateGraph
except ImportError:
    print(
        "LangGraph not installed. Install dependencies with:\n"
        "  pip install -r tools/orchestration/requirements.txt\n\n"
        "Alternatively, follow the manual stage sequence in:\n"
        "  .claude/skills/vertical-slice/SKILL.md",
        file=sys.stderr,
    )
    sys.exit(1)

from providers import ProviderStatus, check_all
from state import AssetStatus, PipelineStage, SliceState


# ------------------------------------------------------------------ node defs


def node_verify_documents(state: SliceState) -> SliceState:
    """Confirm GDD and ADD exist before any generation work begins."""
    missing = [
        path
        for path in (state.gdd_path, state.add_path)
        if not state.doc_exists(path)
    ]
    if missing:
        state.log(
            f"Missing design documents: {missing}. "
            "Run /gen-gdd and /gen-add, then re-run this workflow."
        )
        state.stage = PipelineStage.DESIGN
    else:
        state.log("Design documents verified.")
        state.stage = PipelineStage.PROVIDER_CHECK
    return state


def node_check_providers(state: SliceState) -> SliceState:
    """Populate provider_statuses with sanitized strings. No key values stored."""
    results = check_all()
    state.provider_statuses = {r.name: r.status.value for r in results}

    configured = [r.name for r in results if r.status == ProviderStatus.CONFIGURED]
    missing = [r.name for r in results if r.status == ProviderStatus.MISSING]
    unavailable = [r.name for r in results if r.status == ProviderStatus.UNAVAILABLE]

    state.log(
        f"Providers — configured: {configured}, "
        f"missing: {missing}, unavailable: {unavailable}"
    )
    state.stage = PipelineStage.ASSET_PLAN
    return state


def node_asset_plan(state: SliceState) -> SliceState:
    """Check that design/asset-plan.md exists and has developer confirmation.

    Asset plan authoring is done by the /asset-plan skill. This node
    only reads the confirmation line from the written file.
    """
    plan_path = state.project_root / state.asset_plan_path
    if not plan_path.exists():
        state.log(
            "Asset plan not found. Run /asset-plan to create and confirm it."
        )
        state.stage = PipelineStage.ASSET_PLAN
        return state

    content = plan_path.read_text(encoding="utf-8")
    if "Confirmed by developer: yes" in content:
        state.plan_approved = True
        state.stage = PipelineStage.GENERATION
        state.log("Asset plan confirmed by developer.")
    else:
        state.stage = PipelineStage.AWAITING_APPROVAL
        state.log(
            "Asset plan exists but is not confirmed. "
            "Edit design/asset-plan.md and set 'Confirmed by developer: yes'."
        )
    return state


def _gate_generation(state: SliceState) -> str:
    """Conditional edge: route to generation or halt at approval gate."""
    if state.plan_approved:
        return "generation"
    return "awaiting_approval"


def node_generation_summary(state: SliceState) -> SliceState:
    """Log a summary of the generation stage.

    Actual asset generation is performed by /gen-audio, /gen-3d, /gen-2d.
    This node aggregates their results from the asset registry.
    """
    generated = len(state.generated_assets)
    placeholders = len(state.placeholder_assets)
    failed = len(state.failed_assets)

    state.log(
        f"Generation complete — "
        f"generated: {generated}, placeholders: {placeholders}, failed: {failed}"
    )

    if failed:
        names = [a.name for a in state.failed_assets]
        state.log(f"Failed assets (manual action needed): {names}")

    state.stage = PipelineStage.INTEGRATION
    return state


def node_integration(state: SliceState) -> SliceState:
    """Log integration readiness. File placement is done by generation skills."""
    ready = [
        a for a in state.assets
        if a.status in (AssetStatus.GENERATED, AssetStatus.PLACEHOLDER)
    ]
    state.log(f"Integration: {len(ready)} assets ready for placement.")
    state.stage = PipelineStage.INTEGRATION
    return state


def node_playtest(state: SliceState) -> SliceState:
    """Mark playtest stage reached. Actual playtest runs via /qa skill."""
    state.stage = PipelineStage.PLAYTEST
    state.log("Playtest stage reached. Run /qa to complete the evidence pass.")
    return state


# ------------------------------------------------------------------ graph


def build_graph() -> StateGraph:
    """Assemble the vertical-slice pipeline graph."""
    graph: StateGraph = StateGraph(SliceState)

    graph.add_node("verify_documents", node_verify_documents)
    graph.add_node("check_providers", node_check_providers)
    graph.add_node("asset_plan", node_asset_plan)
    graph.add_node("generation_summary", node_generation_summary)
    graph.add_node("integration", node_integration)
    graph.add_node("playtest", node_playtest)

    graph.set_entry_point("verify_documents")

    graph.add_edge("verify_documents", "check_providers")
    graph.add_edge("check_providers", "asset_plan")

    graph.add_conditional_edges(
        "asset_plan",
        _gate_generation,
        {
            "awaiting_approval": END,
            "generation": "generation_summary",
        },
    )

    graph.add_edge("generation_summary", "integration")
    graph.add_edge("integration", "playtest")
    graph.add_edge("playtest", END)

    return graph


# ------------------------------------------------------------------ entry


def run(project_root: str = ".") -> None:
    """Execute the pipeline and print a run summary."""
    state = SliceState(project_root=Path(project_root))
    compiled = build_graph().compile()
    final: SliceState = compiled.invoke(state)

    print("\n=== Tiny Studio — vertical-slice pipeline ===")
    print(f"Stage reached : {final.stage.value}")
    print(f"Plan approved : {final.plan_approved}")
    print(f"Assets        : {len(final.assets)} total")
    print("\nRun log:")
    for entry in final.run_log:
        print(f"  · {entry}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run the Tiny Studio vertical-slice LangGraph pipeline."
    )
    parser.add_argument(
        "--project-root",
        default=".",
        help="Path to the project root (default: current directory).",
    )
    args = parser.parse_args()
    run(args.project_root)
