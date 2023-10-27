#!/usr/bin/python3
"""
lru caching module
"""
BaseCaching = __import__('base_caching').BaseCaching
from functools import lru_cache
from base_caching import BaseCaching

class LRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.lru_order = []

    def put(self, key, item):
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.lru_order.pop(0)
            del self.cache_data[lru_key]
            if lru_key != key:
                print(f"DISCARD: {lru_key}\n")

        # Add the new item to the cache and lru_order
        self.cache_data[key] = item
        self.lru_order.append(key)

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end of lru_order to mark it as most recently used
        self.lru_order.remove(key)
        self.lru_order.append(key)

        return self.cache_data[key]
