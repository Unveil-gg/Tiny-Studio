"""Shared workflow state for the Tiny Studio vertical-slice pipeline.

All pipeline nodes read from and write to a single SliceState instance.
No API key values are stored here.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any


class AssetStatus(str, Enum):
    PENDING = "pending"
    GENERATED = "generated"
    PLACEHOLDER = "placeholder"
    FAILED = "failed"
    INTEGRATED = "integrated"


class PipelineStage(str, Enum):
    INIT = "init"
    DESIGN = "design"
    PROVIDER_CHECK = "provider_check"
    ASSET_PLAN = "asset_plan"
    AWAITING_APPROVAL = "awaiting_approval"
    GENERATION = "generation"
    INTEGRATION = "integration"
    PLAYTEST = "playtest"
    COMPLETE = "complete"


@dataclass
class AssetEntry:
    """A single asset tracked through the generation pipeline."""

    name: str
    asset_type: str          # "audio" | "3d" | "2d"
    provider: str            # "elevenlabs" | "tripo" | "nano-banana" | "placeholder"
    status: AssetStatus = AssetStatus.PENDING
    output_path: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)
    error: str = ""

    def mark_generated(self, output_path: str, metadata: dict[str, Any]) -> None:
        """Record a successful generation result."""
        self.status = AssetStatus.GENERATED
        self.output_path = output_path
        self.metadata = metadata

    def mark_placeholder(self, reason: str = "") -> None:
        """Downgrade this asset to a placeholder and record the reason."""
        self.status = AssetStatus.PLACEHOLDER
        self.provider = "placeholder"
        self.error = reason

    def mark_failed(self, reason: str) -> None:
        """Record a generation failure."""
        self.status = AssetStatus.FAILED
        self.error = reason


@dataclass
class SliceState:
    """Mutable state shared across all pipeline nodes.

    Rules:
    - No raw API key values are stored here.
    - plan_approved must be set explicitly by developer action.
    - run_log is append-only during a single pipeline run.
    """

    project_root: Path

    stage: PipelineStage = PipelineStage.INIT

    # Design document paths (relative to project_root)
    pillars_path: str = "design/pillars.md"
    gdd_path: str = "design/gdd.md"
    add_path: str = "design/add.md"
    asset_plan_path: str = "design/asset-plan.md"

    # Provider availability (values are sanitized status strings only)
    provider_statuses: dict[str, str] = field(default_factory=dict)

    # Asset registry built from the confirmed asset plan
    assets: list[AssetEntry] = field(default_factory=list)

    # Must be set to True by explicit developer confirmation before generation
    plan_approved: bool = False

    # Playtest notes written by /qa
    playtest_notes: str = ""

    # Append-only log of decisions made during this run
    run_log: list[str] = field(default_factory=list)

    # ------------------------------------------------------------------ helpers

    def log(self, message: str) -> None:
        """Append an entry to the run log."""
        self.run_log.append(message)

    def doc_exists(self, rel_path: str) -> bool:
        """Return True if a project-relative document path exists."""
        return (self.project_root / rel_path).exists()

    @property
    def pending_assets(self) -> list[AssetEntry]:
        return [a for a in self.assets if a.status == AssetStatus.PENDING]

    @property
    def generated_assets(self) -> list[AssetEntry]:
        return [a for a in self.assets if a.status == AssetStatus.GENERATED]

    @property
    def placeholder_assets(self) -> list[AssetEntry]:
        return [a for a in self.assets if a.status == AssetStatus.PLACEHOLDER]

    @property
    def failed_assets(self) -> list[AssetEntry]:
        return [a for a in self.assets if a.status == AssetStatus.FAILED]
