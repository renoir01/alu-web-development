#!/usr/bin/python3
"""
FIFO Caching module - implements FIFO caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache defines:
      - FIFO caching system
      - Max number of items defined by BaseCaching.MAX_ITEMS
    """

    def __init__(self):
        """
        Initialize the FIFO Cache
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Add an item in the cache using FIFO algorithm
        Args:
            key: The key to add
            item: The value to store
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                # Remove first item (FIFO)
                first_key = self.queue.pop(0)
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

            if key not in self.cache_data:
                self.queue.append(key)
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
    