#!/usr/bin/env python3
"""base class for caching"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """a class BasicCache that inherits from BaseCaching"""
    def put(self, key, item):
        """
        Add the item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        return self.cache_data.get(key)
