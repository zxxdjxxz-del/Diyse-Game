"""Small shared helpers used across simulator sections."""
from __future__ import annotations
import math


def round_half_up(value: float) -> int:
    if value < 0:
        return -math.floor(-value + 0.5)
    return math.floor(value + 0.5)
