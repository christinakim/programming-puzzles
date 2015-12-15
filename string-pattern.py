def stringpattern(s):
	strings = []
	if '?' not in s:
		strings.append(s)
		return strings
	else:  
		currentQ = s.index('?')
		newOne = s[:currentQ] + '1' + s[currentQ + 1:]
		newZero = s[:currentQ] + '0' + s[currentQ + 1:]
		print newOne 
		print newZero
		strings.append(stringpattern(newOne))

		strings.append(stringpattern(newZero))

	return strings

def main():
	string1 = "1?1"
	string2 = "??"

	print stringpattern(string1)
	print stringpattern(string2)

if __name__ == '__main__':
	main()

