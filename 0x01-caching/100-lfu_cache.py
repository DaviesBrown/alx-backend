#!/usr/bin/python3
"""
lfu caching module
"""
BaseCaching = __import__('base_caching').BaseCaching
from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """ Least Frequently Used Cache class"""
    def __init__(self) -> None:
        """initialize
        """
        super().__init__()
    
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key == None or item == None:
            pass
        if key in self.cache_data:
            print('jee')
            self.cache_data[key] = item
        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            key_discarded = list(self.cache_data.keys())[0]
            self.cache_data.pop(key_discarded)
            print(self.cache_data)
            print("DISCARD: {}\n".format(key_discarded))
        self.cache_data[key] = item
    
    def get(self, key):
        """ Get an item by key
        """
        if key == None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
