#!/usr/bin/env python3
"""LRU cache module"""

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRU class"""

    def __init__(self):
        super().__init__()
        self.lru = OrderedDict()

    def put(self, key, item):
        """Method to insert a key-value pair."""
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(self.lru.popitem(False)[0]))
            del self.cache_data[self.lru.popitem(False)[0]]

        try:
            del self.lru[key]
        except ValueError:
            pass

        self.lru.append(key)

    def get(self, key):
        """Method to get a value from the cache."""
        return self.cache_data.get(key)
