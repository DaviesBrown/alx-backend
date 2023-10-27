#!/usr/bin/python3
"""
lifo caching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO Cache class"""
    last_item = ""

    def __init__(self) -> None:
        """initialize
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None:
            return
        if item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.last_item = key
        if len(self.cache_data) < BaseCaching.MAX_ITEMS:
            self.cache_data[key] = item
            self.last_item = key
        else:
            self.cache_data.pop(self.last_item)
            print("DISCARD: {}".format(self.last_item))
            self.cache_data[key] = item
            self.last_item = key

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
