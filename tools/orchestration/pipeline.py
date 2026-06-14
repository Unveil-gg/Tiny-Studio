"""Tiny Studio vertical-slice pipeline runner.

No external framework dependencies. The AI agent reading the skill files
does the reasoning; this script tracks state and gates paid calls.

Usage:
    python tools/orchestration/pipeline.py [--project-root PATH] [--json]
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass, field
from pathlib import Path

from providers import ProviderStatus, check_all


@dataclass
class PipelineState:
    """Shared state for one vertical-slice pipeline run."""

    project_root: Path
    gdd_path: str = "design/gdd.md"
    asset_plan_path: str = "design/asset-plan.md"

    provider_statuses: dict[str, str] = field(default_factory=dict)
    plan_approved: bool = False
    assets_generated: list[str] = field(default_factory=list)
    assets_placeholder: list[str] = field(default_factory=list)
    assets_failed: list[str] = field(default_factory=list)
    log: list[str] = field(default_factory=list)
    stage: str = "init"

    def note(self, msg: str) -> None:
        """Append a message to the run log."""
        self.log.append(msg)

    def doc_exists(self, rel_path: str) -> bool:
        """Return True if a project-relative path exists on disk."""
        return (self.project_root / rel_path).exists()

    def doc_text(self, rel_path: str) -> str:
        """Read a project-relative file. Returns empty string if missing."""
        path = self.project_root / rel_path
        return path.read_text(encoding="utf-8") if path.exists() else ""


# ------------------------------------------------------------------ stages


def stage_verify_gdd(state: PipelineState) -> bool:
    """Check that gdd.md exists before any other work begins."""
    if not state.doc_exists(state.gdd_path):
        state.note(
            f"Missing {state.gdd_path}. "
            "Run /start (build mode) to create it."
        )
        state.stage = "needs_gdd"
        return False
    state.note("GDD found.")
    state.stage = "provider_check"
    return True


def stage_check_providers(state: PipelineState) -> None:
    """Populate provider_statuses with sanitized strings. No key values stored."""
    results = check_all()
    state.provider_statuses = {r.name: r.status.value for r in results}
    missing = [r.name for r in results if r.status == ProviderStatus.MISSING]
    unavailable = [r.name for r in results if r.status == ProviderStatus.UNAVAILABLE]
    state.note(
        f"Providers — missing: {missing or 'none'}, "
        f"unavailable: {unavailable or 'none'}"
    )
    state.stage = "asset_plan"


def stage_check_asset_plan(state: PipelineState) -> bool:
    """Check that asset-plan.md exists and has explicit developer confirmation."""
    if not state.doc_exists(state.asset_plan_path):
        state.note(
            "No asset plan found. "
            "Run /asset-plan to create and confirm one."
        )
        state.stage = "needs_plan"
        return False
    content = state.doc_text(state.asset_plan_path)
    if "Confirmed by developer: yes" not in content:
        state.note(
            "Asset plan exists but is not confirmed. "
            "Edit design/asset-plan.md and set 'Confirmed by developer: yes'."
        )
        state.stage = "awaiting_approval"
        return False
    state.plan_approved = True
    state.note("Asset plan confirmed. Ready for generation skills.")
    state.stage = "ready"
    return True


# ------------------------------------------------------------------ entry


def run(project_root: str = ".") -> PipelineState:
    """Execute pipeline checks and return final state."""
    state = PipelineState(project_root=Path(project_root))
    if not stage_verify_gdd(state):
        return state
    stage_check_providers(state)
    stage_check_asset_plan(state)
    return state


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Tiny Studio vertical-slice pipeline checker."
    )
    parser.add_argument(
        "--project-root", default=".", help="Path to the project root."
    )
    parser.add_argument(
        "--json", action="store_true", help="Emit state as JSON."
    )
    args = parser.parse_args()

    state = run(args.project_root)

    if args.json:
        d = asdict(state)
        d["project_root"] = str(state.project_root)
        print(json.dumps(d, indent=2))
    else:
        print("\n=== Tiny Studio — pipeline check ===")
        print(f"Stage         : {state.stage}")
        print(f"Plan approved : {state.plan_approved}")
        print("\nProviders:")
        for name, status in state.provider_statuses.items():
            print(f"  {name:<20} {status}")
        print("\nLog:")
        for entry in state.log:
            print(f"  · {entry}")


if __name__ == "__main__":
    main()
