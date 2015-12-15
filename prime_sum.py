def is_prime(n):
	if n < 2:
		return False
	
	arr = [n % i for i in range(2, n)]
	return all(arr)

def sum_prime(target):
	b=1
	d=0
	#generates a list of numbers.
	while b<target:
	    b=b+1
	    if is_prime(b):
	        d=d+b
	print d
sum 