#[1,2,[3,4,[5,6],7,[8,[9]]],10]
#[1,2,3,4,5,6,7,8,9,10]

def itr_flat(li):
	stack = []
	for item in li:
		if isinstance(item, list):
			stack = stack + itr_flat(item)
		else:
			stack.append(item)
	return stack


def flatten(array):
	result = []
	string_arr = str(array).replace('[', '').replace(']', '')
	flat_list =string_arr.split(',')
	for i in flat_list:
		result.append(int(i))
	return result

    

def main():
	a = [1,2,[3,4,[5,6],7,[8,[9]]],10]
	#print flat(toflat)
	print flatten(a)
	#print better_flatten(a)
	print itr_flat(a)

if __name__ == "__main__":
	main()