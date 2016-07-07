# capitalize_sentence.py
"""
Given a sentence, how would you transform each word to start with a capital letter.
"""

def capitalize_sentence(string):
	result = ''
	result += string[0].upper() 
	i = 1
	while i < len(string):
		if string[i] == ' ':
			result += ' ' + (string[i+1].upper())
			i += 2
		else:
			result +=string[i]
			i += 1
		
	
	return result

def main():
	print capitalize_sentence('hello from the other side')

if __name__ == '__main__':
	main()