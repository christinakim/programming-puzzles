"""Given a message "one two three four five six seven eight nine", chop it in chunks(no exceed the give buffer size) and print out to the screen. Need to maintain the word and do not chop it off. I.E.: buffer size is 15 one two three (1/4) four five six (2/4) seven eight (3/4) nine (4/4) 
"""

def word_break(s):
	p = s.split(' ')
	msgs = []
	buff_size = 0
	msg = ''

	for word in p:
		if buff_size + len(word) > 15:
			buff_size = 0
			msgs.append(msg)
			msg = word
		else:
			buff_size = buff_size + len(word) + 1
			if len(msg) == 0:
				msg = word 
			else:
				msg = msg + ' ' + word

	msgs.append(msg)

	return msgs 

def main():
	s= "one two three four five six seven eight nine"
	print word_break(s)

if __name__ == '__main__':
	main()
