#!/usr/bin/python3
"""
LFU Caching module - implements LFU caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache defines:
      - LFU caching system
      - Max number of items defined by BaseCaching.MAX_ITEMS
    """

    def __init__(self):
        """
        Initialize the LFU Cache
        """
        super().__init__()
        self.usage_count = {}
        self.usage_order = []

    def put(self, key, item):
        """
        Add an item in the cache using LFU algorithm
        Args:
            key: The key to add
            item: The value to store
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                # Find least frequently used items
                min_freq = min(self.usage_count.values())
                lfu_keys = [k for k, v in self.usage_count.items() if v == min_freq]
                
                # If multiple items have same frequency, use LRU
                lfu_key = None
                for k in self.usage_order:
                    if k in lfu_keys:
                        lfu_key = k
                        break

                del self.cache_data[lfu_key]
                del self.usage_count[lfu_key]
                self.usage_order.remove(lfu_key)
                print(f"DISCARD: {lfu_key}")

            self.cache_data[key] = item
            self.usage_count[key] = self.usage_count.get(key, 0) + 1
            
            if key in self.usage_order:
                self.usage_order.remove(key)
            self.usage_order.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache
        Args:
            key: The key to look for
        Returns:
            The value associated with the key if it exists, None otherwise
        """
        if key is not None and key in self.cache_data:
            self.usage_count[key] = self.usage_count.get(key, 0) + 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None
