#!/usr/bin/env python3
"""LLRU cache modulule"""
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRU class"""
    def __init__(self):
        super().__init__()
        self.lru = OrderedDict()
        
    def put(self, key, item):
        """method to insert key"""
        if key is None or item is None:
          return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
          print("DISCARD: {}".format(self.lru[0]))
          del self.cache_data[self.lru[0]]
          self.cache_data.popitem(last=False)

        try:
          self.lru.remove(key)

        except ValueError:
          pass

        self.lru.append(key)

    def get(self,key):
      """method to get key"""
      return self.cache_data.get(key)
