# Caching System Implementation

## Description
This project implements different caching algorithms in Python. Each implementation inherits from a base caching class and demonstrates various cache replacement policies.

## Caching Algorithms Implemented
1. Basic Cache (No limit)
2. FIFO (First In First Out)
3. LIFO (Last In First Out)
4. LRU (Least Recently Used)
5. MRU (Most Recently Used)
6. LFU (Least Frequently Used)

## Files Structure
- `base_caching.py`: Base class with fundamental caching system structure
- `0-basic_cache.py`: Basic caching system with no limit
- `1-fifo_cache.py`: FIFO caching system
- `2-lifo_cache.py`: LIFO caching system
- `3-lru_cache.py`: LRU caching system
- `4-mru_cache.py`: MRU caching system
- `100-lfu_cache.py`: LFU caching system

## Requirements
- Python 3.7
- Ubuntu 18.04 LTS
- pycodestyle 2.5

## Class Descriptions

### BaseCaching
- Parent class for all caching systems
- Defines MAX_ITEMS constant (4)
- Provides basic structure for cache data storage

### BasicCache
- No limit on storage
- Simple key-value storage system
- Methods:
  - `put(key, item)`: Add item to cache
  - `get(key)`: Retrieve item from cache

### FIFOCache
- Maximum of 4 items
- Removes first item added when cache is full
- Prints "DISCARD:" message when removing items

### LIFOCache
- Maximum of 4 items
- Removes last item added when cache is full
- Prints "DISCARD:" message when removing items

### LRUCache
- Maximum of 4 items
- Removes least recently used item when cache is full
- Prints "DISCARD:" message when removing items

### MRUCache
- Maximum of 4 items
- Removes most recently used item when cache is full
- Prints "DISCARD:" message when removing items

### LFUCache
- Maximum of 4 items
- Removes least frequently used item when cache is full
- Uses LRU for ties in frequency
- Prints "DISCARD:" message when removing items

## Usage
Each cache implementation can be tested using its corresponding main file:
```python
#!/usr/bin/python3
BasicCache = __import__('0-basic_cache').BasicCache
my_cache = BasicCache()
my_cache.print_cache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
print(my_cache.get("A"))