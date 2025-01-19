#!/usr/bin/python3
""" BasicCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines:
      - Caching system with no limit
      - Inherits from BaseCaching
    """

    def put(self, key, item):
        """ Add an item in the cache
        Args:
            key: key to add
            item: value to add
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        Args:
            key: key to look for
        Returns:
            value associated with key if it exists, None otherwise
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None