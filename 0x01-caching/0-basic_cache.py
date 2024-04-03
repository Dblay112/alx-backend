#!/usr/bin/env python3
"""base class for caching"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """a class BasicCache that inherits from BaseCaching"""
    def put(self, key, item):
        """method to add an item to the cache"""
        if key is None or item is None:
            return
        return self.cache_data[key] = item

    def get(self, key):
        """method to retrieve an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get[key]
