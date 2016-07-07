def smallest(k):
	smallest = 10000
	for i in k:
		print i
		if i < smallest:
			smallest = i

	return smallest

if __name__ == '__main__':
	print smallest([2,3,4,5,1])
