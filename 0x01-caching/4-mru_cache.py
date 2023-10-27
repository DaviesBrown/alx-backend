#!/usr/bin/python3
"""
mru caching module
"""
BaseCaching = __import__('base_caching').BaseCaching
from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """ Most Recently Used Cache class"""
    def __init__(self) -> None:
        """initialize
        """
        super().__init__()
    
    def put(self, key, item):
        if key is None or item is None:
            return

        # Check if the cache is full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = list(self.cache_data.keys())[-1]  # Get the MRU key
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}\n")

        # Add the new item to the cache
        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
