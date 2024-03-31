#!/usr/bin/env python3
"""interpreter used"""

from typing import Tuple
import csv
import math
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
    """Paginate the dataset correctly and return the appropriate page.

    Args:
      page (int, optional): Page number.
      page_size (int, optional): Total page size.

    Returns:
      List[List]: The appropriate page of the dataset.
    """
    assert isinstance(page, int) and page > 0
    assert isinstance(page_size, int) and page_size > 0

    data_len = len(self.dataset())
    if page > data_len or page_size > data_len:
      return []

    start_index, end_index = self.index_range(page, page_size)
    return self.dataset()[start_index:end_index]
