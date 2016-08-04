"""
Return the coins combination with the minimum number of coins.Time complexity O(MN), where M is the target value and N is the number of distinct coins. Space complexity O(M).

Return the coins combination with the minimum number of coins.Time complexity O(MN), where M is the target value and N is the number of distinct coins. Space complexity O(M).  

constraints:

"""

def change_maker(n, target, combinations = {}):
	print target 
	if target in combinations.keys():
		return combinations[target]

	else: 
		if target == 0:
			combinations[0] = []
			return combinations[0]
		else:
			combo = []
			num_of_coins = 0		
			i = 0
			while len(n) > i and target >= n[i]:
				combo.append(change_maker(n, target - n[i], combinations) + [n[i]])
				i += 1
			if combo:
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
	print change_maker([1,4,5,6], 11)

if __name__ == '__main__':
	main()