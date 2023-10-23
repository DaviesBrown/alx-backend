#!/usr/bin/env python3
"""
server class
"""
import csv
import math
from typing import Any, Dict, List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """init"""
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
    
    @property
    def datasets(self):
        """get all dataset"""
        return self.dataset()

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get page from dataset"""
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        (start, end) = index_range(page, page_size)
        data = self.datasets
        if data and data[start: end]:
            return data[start: end]
        return []
    

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """get heyper pagination"""
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.datasets) / page_size)  
        page_info = {
            'page_size': page_size if data else 0,
            'page': page,
            'data': data,
            'next_page': page + 1 if data else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
        return page_info
