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
class TTHashEntry(object):
    def __init__(self, time, key, value):
        self.time = time
        self.key = key
        self.value = {}
        
           
class TTHash(object):
    
    def __init__(self):
        self.keys = None
        self.value = None
        self.table = {}
    
    def put(time, key, value):
        
    
    def get(time, key):
        