#!/usr/bin/env python3
"""interpreter used"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing a start
    index and an end index corresponding to the range of indexes.
    Args:
    page: Current page number.
    page_size: Items per page number.
    Returns:
    A tuple containing the start and end index for the current page.
    """
    data = 19419
    s_index = (page - 1) * page_size
    e_index = min(s_index + page_size, data)
    return s_index, e_index
