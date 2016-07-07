def isPalindrome(word):
	reverse_str = word[::-1]
	print reverse_str
	if word == reverse_str:
		return True
	return False

def betterPal(word):
	for i in range(len(word)/2):
		print i
		if word[i] != word[len(word)-i-1]:
			return False
	return True

def main():
	str1 = "abba"
	assert isPalindrome(str1) == True
	assert betterPal("abbba") == True

if __name__ == '__main__':
	main()