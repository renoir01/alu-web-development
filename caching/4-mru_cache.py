#!/usr/bin/python3
"""
MRU Caching module - implements MRU caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache defines:
      - MRU caching system
      - Max number of items defined by BaseCaching.MAX_ITEMS
    """

    def __init__(self):
        """
        Initialize the MRU Cache
        """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """
        Add an item in the cache using MRU algorithm
        Args:
            key: The key to add
            item: The value to store
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                # Remove most recently used item
                mru_key = self.usage_order.pop()
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")

            if key in self.usage_order:
                self.usage_order.remove(key)
            self.usage_order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache
        Args:
            key: The key to look for
        Returns:
            The value associated with the key if it exists, None otherwise
        """
        if key is not None and key in self.cache_data:
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None
