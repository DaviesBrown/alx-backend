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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        Gets the results per page of the given page
        '''
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        page_list = []
        results = self.dataset()
        indexes = index_range(page, page_size)
        try:
            for i in range(indexes[0], indexes[1]):
                page_list.append(results[i])
        except IndexError:
            pass
        return page_list

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        '''
        Gets the results per page of the given page and returns a dictionary
        '''
        hyper_dict = {}
        page_list = self.get_page(page, page_size)
        act_page_size = len(page_list)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        if page < total_pages:
            nextp = page + 1
        else:
            nextp = None

        if page != 1:
            prev = page - 1
        else:
            prev = None
        hyper_dict["page_size"] = act_page_size
        hyper_dict["page"] = page
        hyper_dict["data"] = page_list
        hyper_dict["next_page"] = nextp
        hyper_dict["prev_page"] = prev
        hyper_dict["total_pages"] = total_pages
        return hyper_dict
