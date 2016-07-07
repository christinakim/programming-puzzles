# reverse_string.py
"""
Given a sentence, reverse the words. 
i.e. christina 
"""

def reverse_buffer_string(string):
	length = len(string)
	print len
	print string
	while length > 0:
		reversestring = string.pop()
		length -= 1
	return reversestring

def rv_str(string):
	return string[::-1]

def main():
	print reverse_buffer_string('christina')
	print rv_str('christina')

if __name__ == '__main__':
	main()
