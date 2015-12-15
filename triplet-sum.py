def triplets(N, T):
    N = sorted(N)
    result = []

    for i in range(len(N)):
        for j in range(i+1, len(N)): 
          for k in range(j+1, len(N)): 
            if N[i]+N[j]+N[k]>T:
              result.append([N[i], N[j], N[k]])

    return result

def main():
	n = [1,2,3,4,5,6]
	print triplets(n, 12)

if __name__ == '__main__':
	main()
