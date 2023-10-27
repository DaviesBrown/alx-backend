#!/usr/bin/python3
"""
fifo caching module
"""
BaseCaching = __import__('base_caching').BaseCaching
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """ FIFO Cache class"""
    def __init__(self) -> None:
        """initialize
        """
        super().__init__()
    
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key == None or item == None:
            pass
        if key in self.cache_data or len(self.cache_data) < BaseCaching.MAX_ITEMS:
            self.cache_data[key] = item
        else:
            key_discarded = list(self.cache_data)[0]
            self.cache_data.pop(key_discarded)
            print("DISCARD: {}".format(key_discarded))
            self.cache_data[key] = item
    
    def get(self, key):
        """ Get an item by key
        """
        if key == None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
