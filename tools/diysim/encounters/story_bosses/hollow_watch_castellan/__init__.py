"""Hollow Watch Castellan repo-backed encounter simulator."""

from .policy import SmartPolicyConfig
from .repo_loader import (
    HollowWatchRepoData,
    collect_hollow_watch_source_gaps,
    load_hollow_watch_repo_data,
)
from .runtime import (
    HollowWatchOutcome,
    HollowWatchSummary,
    run_hollow_watch_smart,
    simulate_hollow_watch_smart,
)

__all__ = [
    "HollowWatchOutcome",
    "HollowWatchRepoData",
    "HollowWatchSummary",
    "SmartPolicyConfig",
    "collect_hollow_watch_source_gaps",
    "load_hollow_watch_repo_data",
    "run_hollow_watch_smart",
    "simulate_hollow_watch_smart",
]
