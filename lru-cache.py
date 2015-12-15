"""
LRU cache
"""
class Node:
  def __init__(self, key, value):
    self.value = value
    self.key = key
    self.next = None
    self.prev = None

class LRU:
  def __init__(self, size):
    self.cache = {}
    self.size = size
    self.head = None
    self.tail = None

  def lookup(self, key):
    self.cache.get(key, None)

  def set(self, key, value):
    if len(self.cache) < self.size: 
      self.cache[key] = value
