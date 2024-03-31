#!/usr/bin/env python3
"""I prefer interpreter being used here"""
from typing import Dict, List, String, Number, Any
import math


def hyper(page: int = 1, page_size: int = 10) -> Dict[str, Any]:
    """Returns a dictionary containing hypermedia information."""
    data = get_page(page, page_size)
    data_len = len(data)
    total_pages = math.ceil(len(dataset()) / page_size)
    next_page = page + 1 if page < total_pages else None
    prev_page = page - 1 if page > 1 else None
    return {
        'page_size': page_size,
        'page': page,
        'data': data,
        'next_page': next_page,
        'prev_page': prev_page,
        'total_pages': total_pages
    }

def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Method to get a page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()

        if end >= len(data):
            return []

        return data[start:end]
