#!/usr/bin/env python3
"""
task 8. Complex types - functions
Write a type-annotated function make_multiplier
that takes a float multiplier as argument
and returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier."""
    def multiplier_function(number: float) -> float:
        """Return a float multiplied by multiplier."""
        return number * multiplier
    return multiplier_function
