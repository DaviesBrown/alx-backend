#!/usr/bin/python3
"""
lru caching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ Least Recently Used Cache class"""

    def __init__(self):
        """initialize
        """
        super().__init__()
        self.lru_order = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            lru_key = self.lru_order.pop(0)
            del self.cache_data[lru_key]
            if lru_key != key:
                print(f"DISCARD: {lru_key}\n")
        self.cache_data[key] = item
        self.lru_order.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.lru_order.remove(key)
        self.lru_order.append(key)
        return self.cache_data[key]
