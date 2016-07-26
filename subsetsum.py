def subsetsum(array, num):
    if sum(array) == num:
        return array
    if len(array) > 1:
        for subset in (array[:-1], array[1:]):
            result = subsetsum(subset, num)
            if result is not None:
                return result

def main():
	print subsetsum([1,2,3,4,5], 7)

if __name__ == '__main__':
	main()