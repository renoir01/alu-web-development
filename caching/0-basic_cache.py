#!/usr/bin/python3
"""
BasicCache module - implements a basic caching system with no limit
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache defines:
      - Basic caching system with no limit
      - Inherits from BaseCaching
    """

    def put(self, key, item):
        """
        Add an item in the cache
        Args:
            key: The key to add
            item: The value to store
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache
        Args:
            key: The key to look for
        Returns:
            The value associated with the key if it exists, None otherwise
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
