#!/usr/bin/env python3
from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching
    and implements an LFU (Least Frequently Used)
    caching system.
    """
    def __init__(self):
        """
        Initialize the LFUCache instance.
        """
        super().__init__()
        self.frequency = defaultdict(int)
        self.usage_order = defaultdict(OrderedDict)

    def put(self, key, item):
        """
        Add an item in the cache.
        If the number of items in the cache is greater
        than BaseCaching.MAX_ITEMS, it discards the least
        frequently used item before adding the new item.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self._update_frequency(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self._evict_lfu_item()
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order[1][key] = None

    def get(self, key):
        """
        Get an item by key.
        Returns the item if the key exists in the cache,
        otherwise returns None.
        """
        if key is None or key not in self.cache_data:
            return None
        self._update_frequency(key)
        return self.cache_data[key]

    def _update_frequency(self, key):
        """
        Update the frequency and usage order of a given key.
        """
        freq = self.frequency[key]
        self.frequency[key] += 1
        del self.usage_order[freq][key]
        if not self.usage_order[freq]:
            del self.usage_order[freq]
        self.usage_order[freq + 1][key] = None

    def _evict_lfu_item(self):
        """
        Evict the least frequently used item from the cache.
        """
        lfu_freq = min(self.usage_order)
        lfu_key, _ = self.usage_order[lfu_freq].popitem(last=False)
        if not self.usage_order[lfu_freq]:
            del self.usage_order[lfu_freq]
        del self.cache_data[lfu_key]
        del self.frequency[lfu_key]
        print(f"DISCARD: {lfu_key}")
