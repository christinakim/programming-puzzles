#Given a system, a number N, represent item #, and several   numbers that represent the factor that it will process the item # if the item can be a multiple of it. Found that how many items cannot be processed? Ex: Given [2, 5] and N = 10. 2, 4, 6, 8, 10, 5 can be process the remaining number is 1 3 7 9, so return 4

def find_mult(n, lis):
	multiples = set()
	for num in lis:
		i=0
		while i < n and i*num < n:
			multiples.add(i*num)
			i += 1 

	return n - len(multiples)

print find_mult(10, [2,5])