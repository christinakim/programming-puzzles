"""Class that represents a doubly-linked list node."""
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache(object):
    def __init__(self, size):
        """Constructor for LRU Cache."""
        self.cache = {}
        self.size = size
        self.head = None
        self.tail = None

    def set(self, key, value):
        """Add a key, value mapping to cache."""
        if len(self.cache) == self.size and key not in self.cache:
            self._evict_head()

        if key in self.cache:
            self._remove_node(self.cache[key])

        new_node = Node(key, value)
        self.cache[key] = new_node


        if self.head == None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def get(self, key):
        """Lookup the value for a key in the cache."""
        try:
            node = self.cache[key]
        except KeyError:
            print 'Key {key} not found!'.format(key=key)
            return -1

        value = node.value

        if node == self.tail:
            return value

        self._remove_node(node)

        # update tail
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

        return value

    def _evict_head(self):
        """Evict head from linked list and remove entry from cache."""
        key = self.head.key
        if self.size > 1:
            self.head = self.head.next
            self.head.prev = None
            # delete from cache
        del self.cache[key]

    def _remove_node(self, node):
        """Remove a given node from the linked list."""
        if node == self.head:
            next_node = self.head.next
            if next_node != None:
                next_node.prev = None
                self.head = next_node

        elif node == self.tail:
            prev_node = self.tail.prev
            if prev_node != None:
                prev_node.next = None
                self.tail = prev_node

        else:
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node




def main():
    cache = LRUcache(3)
    cache.set('name', 'Christina')
    cache.set('age', '21')
    cache.set('location', 'Evanston')
    cache.set('location', 'SF')

    assert cache.get('age') == '21'
    assert cache.get('location') == 'SF'
    assert cache.get('name') == 'Christina'

    cache.add('last_name', 'Kim')
    assert cache.get('last_name') == 'Kim'
    assert cache.get('age') == -1

    print 'All tests pass!'

if __name__ == '__main__':
    main()
