def isPrime(n):
   if n == 1:
      return False
   for t in range(2,n):
      if n % t == 0:
         return False
   return True

for n in [0, 1, 8, 7, 64]:
   print isPrime

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

def split_list(a_list):
    half = len(a_list)/2
    return a_list[:half], a_list[half:]

A = [1,2,3,4,5,6]
B, C = split_list(A)




# Check if two strings are anagrams
import sys

# read first line of input from stdin and store in string1
string1 = sys.stdin.readline()
# read second line of input from stdin and store in string2
string2 = sys.stdin.readline()

# initialize an empty dictionary/ hash for each string1
# the key will be each character in the string and the value will be the number of times that character appears
string1_dict = {}
string2_dict = {}
 
# add each character in string1 to string1_dict.
# if it already exists in the dictionary, simply increase it's count
for c in string1:
    if c in string1_dict:
        # increase count
        string1_dict[c] += 1
    else:
        # add to dictionary
        string1_dict[c] = 1

for c in string2:
    if c in string2_dict:
        # increase count
        string2_dict[c] += 1
    else:
        # add to dictionary
        string2_dict[c] = 1
        
# compare both the dictionaries
# if the dictionaries are equal, they are anagrams!
if cmp(string1_dict, string2_dict) == 1:
    print "Anagrams!"
else:
    print "Not anagrams!"
