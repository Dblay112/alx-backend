#!/usr/bin/env python3
"""base class for caching"""
from base_caching import BaseCaching


class BasicCache(Basecaching):
    """a class BasicCache that inherits from BaseCaching"""
    def put(self, key, item):
        """method to add an item to the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """method to retrieve an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        self.cache_data[key]
