#!/usr/bin/env python3
"""
helper function
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    returns a tuple of start and end index for pagination
    parameters
    """
    end = page * page_size
    start = end - page_size
    return (start, end)