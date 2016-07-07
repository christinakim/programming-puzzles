# reverse_sentence.py
"""
Given a sentence, reverse the words. 
i.e. The sky is blue.
Blue is sky the. 
"""

def reverse_sentence(string):
	string = string[:-1]
	words = string.split(' ')
	words.reverse()

	reverse_sent = ' '.join(words)
	reverse_sent += '.'
	reverse_sent = reverse_sent.capitalize()
	return reverse_sent

def main():
	string = 'The sky is blue.'
	result = 'Blue. is sky the'
	print reverse_sentence(string)

if __name__ == '__main__':
	main()

