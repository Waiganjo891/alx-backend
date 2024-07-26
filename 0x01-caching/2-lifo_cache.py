#!/usr/bin/python3
"""
LIFO Caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    a class LIFOCache that inherits from BaseCaching
    """
    def __init__(self):
        """
        self.cache_data - dictionary from the
        parent class BaseCaching
        """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.stack.remove(key)
        self.cache_data[key] = item
        self.stack.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.stack.pop(-2)
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

    def get(self, key):
        """
        Get an item by key
        """
        return self.cache_data.get(key, None)
