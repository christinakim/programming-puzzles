def main():
	f = open('duplicates.txt', 'r+')
	lines = f.readlines()
	print lines
	uniqueSet = set()
	f.seek(0)
	for i in lines:
		print i
		if i not in uniqueSet:
			uniqueSet.update([i])
			print uniqueSet
			f.write(i)
	f.truncate()
	f.close()



if __name__ == '__main__':
	main()