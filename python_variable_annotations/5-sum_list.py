#!/usr/bin/env python3
""" list of floats """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of floats in a list.

    Args:
        input_list (List[float]): The list of floats.

    Returns:
        float: The sum of floats in the list.
    """
    return sum(input_list)
