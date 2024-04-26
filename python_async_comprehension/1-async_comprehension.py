#!/usr/bin/env python3
"""Async Comprehensions"""
import asyncio
from typing import List
from async_generator import async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using async comprehension over async_generator."""
    return [number async for number in async_generator()]
