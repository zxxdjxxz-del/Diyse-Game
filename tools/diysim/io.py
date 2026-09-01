"""Compatibility facade for sectioned simulator input loaders.

New loader implementation belongs in the section that owns the input type:
- battle scenarios: `scenarios/io.py`
- progression routes: `progression/io.py`
"""

from .progression.io import load_progression_route
from .scenarios.io import load_advanced_scenario, load_scenario

__all__ = [
    "load_advanced_scenario",
    "load_progression_route",
    "load_scenario",
]
