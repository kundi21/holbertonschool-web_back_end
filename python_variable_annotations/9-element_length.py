#!/usr/bin/env python3
"""
task 9. Let's duck type an iterable object
Annotate the below functions parameters and
return values with the appropriate types.
def element_length(lst):
    return [(i, len(i)) for i in lst]
"""
from typing import Iterable, List, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Sequence[int]]:
    """
    Returns a list of tuples with the length of each element
    """
    return [(i, len(i)) for i in lst]
