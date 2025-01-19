#!/usr/bin/python3
"""
LIFO Caching module - implements LIFO caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache defines:
      - LIFO caching system
      - Max number of items defined by BaseCaching.MAX_ITEMS
    """

    def __init__(self):
        """
        Initialize the LIFO Cache
        """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        Add an item in the cache using LIFO algorithm
        Args:
            key: The key to add
            item: The value to store
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                # Remove last item (LIFO)
                last_key = self.stack.pop()
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

            if key in self.cache_data:
                self.stack.remove(key)
            self.stack.append(key)
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
