#!/usr/bin/env python3
""" String and int/float to tuple """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with the string k and the square of the int/float v.

    Args:
        k (str): The string key.
        v (Union[int, float]): The integer or float value.

    Returns:
        Tuple[str, float]: A tuple containing the string k and the square of v.
    """
    return k, float(v ** 2)
