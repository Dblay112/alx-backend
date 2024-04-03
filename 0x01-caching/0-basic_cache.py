#!/usr/bin/env python3
"""base class for caching"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """a class BasicCache that inherits from BaseCaching"""
    def put(self, key, item):
        """method to add an item to the cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """method to retrieve an item from the cache"""
        return self.cache_data.get[key]
