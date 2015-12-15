# Alternating Characters
# Shashank likes strings in which consecutive characters are different.
# For example, he likes ABABA, while he doesn't like ABAA. Given a string containing characters A and B only,
# he wants to change it into a string he likes. To do this, he is allowed to delete the characters in the string.
# Your task is to find the minimum number of required deletions.

import sys

cases = int(sys.stdin.readline())
array = []

# read all the lines from stdin
for i in range(cases):
	temp = sys.stdin.readline()
	array.append(temp.rstrip())

def make_alternate(string):
	# create array to hold indices of characters that need to be deleted from the string
	# we do this so that we don't shorten the string in the for loop, hence avoiding index out of range errors
	indices = []
	prev = ''
	for i in range(len(string)):
		c = string[i]
		if c == prev:
			# add to the array with all the items to be deleted from string
			indices.append(i)
		else:
			# only update prev when you've found the next character you want to keep in your string
			prev = c

	# return the size of the array because you only need number of deletions
	return len(indices)

for s in array:
	print make_alternate(s)