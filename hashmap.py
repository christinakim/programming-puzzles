class HashTable(object):

    def __init__(self):
    	self.table = [None] * 256

    def _get_value(self, key):
        total = 0
        for i in range(len(key)):
            total += ord(key[i]) * (7**i)
        return (len(key) * total) % 256

    def insert(self, key):
        val = self._get_value(key)
        if self.table[val] == None:
            self.table[val] = key
        else:
            if type(self.table[val]) == list:
                self.table[val].append(key)
            else:
                self.table[val] = [self.table[val], key]

    def delete(self, key):
        val = self._get_value(key)
        if self.table[val] != None:
            if type(self.table[val]) == list:
                i = self.table[val].index(key)
                self.table[val][i] = None
            else:
                self.table[val] = None
        else:
            KeyError()

    def lookup(self, key):
        found = False
        val = self._get_value(key)
        if type(self.table[val]) == list:
            found = key in self.table[val]
        else:
            found = self.table[val] == key
        return found