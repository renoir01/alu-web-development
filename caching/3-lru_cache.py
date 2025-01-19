#!/usr/bin/python3
"""
LRU Caching module - implements LRU caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache defines:
      - LRU caching system
      - Max number of items defined by BaseCaching.MAX_ITEMS
    """

    def __init__(self):
        """
        Initialize the LRU Cache
        """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """
        Add an item in the cache using LRU algorithm
        Args:
            key: The key to add
            item: The value to store
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                # Remove least recently used item
                lru_key = self.usage_order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

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
