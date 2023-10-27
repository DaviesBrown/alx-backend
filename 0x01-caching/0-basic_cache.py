#!/usr/bin/python3
"""
basic cache module
"""
BaseCaching = __import__('base_caching').BaseCaching
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """ Basic Cache class"""
    def __init__(self) -> None:
        """initialize
        """
        super().__init__()
    
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key == None:
            pass
        if item == None:
            pass
        self.cache_data[key] = item
    
    def get(self, key):
        """ Get an item by key
        """
        if key == None:
            pass
        if key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
