## This is the text editor interface. 
## Anything you type or change here will be seen by the other person in real time.
"""
put (1, K, "A")
put(2, K, "B")
put(3, K, "C")

get(1, K) = "A"
get(1.5, K) = "A"
get(2, K) = "B"
get(2.5, K) = "B"
get(3.5, K) = "C"
get(0, K) = NULL or NotFoundException

"""
import collections 
import math 

class TTHash(object):
    
    def __init__(self):
        self.times = {}

    def put(self, time, key, value):
        self.times[time] = {key: value}
    
    def get(self, time, key):
        if time  in self.times:
            hashmap = self.times[time]
            return hashmap[key]
        else:
            if int(math.floor(time)) in self.times:
                hashmap = self.times[int(math.floor(time))]
                return hashmap[key]
            else:
                return None


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


def main():
    tth = TTHash()
    tth.put (1, 'K', "A")
    tth.put(3, 'K', "C")

    assert tth.get(1, 'K') == "A"
    assert tth.get(1.5, 'K') == "A"
    assert tth.get(2, 'K') == "A"
    assert tth.get(2.5, 'K') == "A"
    assert tth.get(3.5, 'K') == "C"
    assert tth.get(0, 'K') == None

if __name__ == '__main__':
    main()