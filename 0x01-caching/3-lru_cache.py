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
        self.keys = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if (key and item):
            self.cache_data[key] = item
            if key in self.keys:
                self.keys.remove(key)
                self.keys.append(key)
            else:
                self.keys.append(key)
            if len(self.keys) > self.MAX_ITEMS:
                erase = self.keys.pop(0)
                del self.cache_data[erase]
                print('DISCARD: {}'.format(erase))

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.keys.remove(key)
        self.keys.append(key)
        return self.cache_data[key]
