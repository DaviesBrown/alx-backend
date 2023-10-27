#!/usr/bin/python3
"""
lifo caching module
"""
BaseCaching = __import__('base_caching').BaseCaching
from base_caching import BaseCaching

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
        if key == None or item == None:
            pass
        if key in self.cache_data or len(self.cache_data) < BaseCaching.MAX_ITEMS:
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
        if key == None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]

my_cache = LIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()