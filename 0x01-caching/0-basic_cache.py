#!/usr/bin/env python3
"""
constants of your caching system
where your data are stored (in a dictionary)
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
