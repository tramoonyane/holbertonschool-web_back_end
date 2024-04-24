#!/usr/bin/env python3
""" Duck type an iterable object  """
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Calculate the length of each element in a list of strings.

    Args:
        lst (List[str]): The list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples where each tuple
        contains a string from lst and its length.
    """
    return [(i, len(i)) for i in lst]
