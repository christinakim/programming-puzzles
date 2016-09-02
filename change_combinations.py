"""
Return the coins combination with the minimum number of coins.Time complexity O(MN), where M is the target value and N is the number of distinct coins. Space complexity O(M).

Return the coins combination with the minimum number of coins.Time complexity O(MN), where M is the target value and N is the number of distinct coins. Space complexity O(M).  

constraints:

"""
import timeit


def change_maker(n, target, combinations = {}):
	if target in combinations:
		return combinations[target]

	else: 
		if target == 0:
			combinations[0] = []
			return combinations[0]
		else:
			"""
			combo = []

			i = 0
			while len(n) > i and target >= n[i]:
				combo.append(change_maker(n, target - n[i], combinations) + [n[i]])
				i += 1
			"""
			combo = [change_maker(n, target - n[i], combinations) + [n[i]] for i in range(len(n)) if target >= n[i]]	

			min_num = len(combo[0])
			min_index = 0
			if len(combo) > 1:
				combo = combo[1:]
				for j in range(len(combo)):
					if len(combo[j]) < min_num:
						min_num = len(combo[j])
						min_index = j

			combinations[target] = combo[min_index]

			return combinations[target]


def main():
	n = [x for x in range(100)]
	print timeit.timeit("change_maker([1,2,5,6], 1)", setup = "from __main__ import change_maker")
	print timeit.timeit("change_maker([1,2,5,6], 10)", setup = "from __main__ import change_maker")

	print timeit.timeit("change_maker([1,2,5,6], 1000)", setup = "from __main__ import change_maker")
if __name__ == '__main__':
	main()