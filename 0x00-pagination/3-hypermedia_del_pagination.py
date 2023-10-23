#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
from typing import Dict, List, Set


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """init"""
        self.__dataset = None
        self.__indexed_dataset = None

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
    def index_data(self):
        """get indexed data"""
        return self.__indexed_dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset
    
    def get_hyper_index(self,
                        index: int = None,
                        page_size: int = 10) -> Dict:
        """
        if between two queries, certain rows are removed from
        the dataset, the user does not miss items from dataset
        when changing page
        """
        if index is not None:
            assert 0 <= index < len(self.__indexed_dataset)
            current_index = index
            next_index = current_index + page_size

            deleted_indices: Set = set()
            data = []
            for i in range(current_index, next_index):
                if i in deleted_indices:
                    deleted_indices.remove(i)
                elif i not in self.__indexed_dataset:
                    deleted_indices.add(i)
            next_index += len(deleted_indices)

            for i in range(current_index, next_index):
                if i not in deleted_indices and \
                    i in self.__indexed_dataset:
                    data.append(self.__indexed_dataset[i])

            return {
                'index': index,
                'next_index': next_index,
                'page_size': page_size,
                'data': data
            }
