def triplets(N, T):
    N = sorted(N)
    result = []

    for i in range(len(N)):
        for j in range(i+1, len(N)): 
          for k in range(j+1, len(N)): 
            if N[i]+N[j]+N[k]>T:
              result.append([N[i], N[j], N[k]])

    return result

def better_triplets(N, target):
  N = sorted(N)

  for i in range(len(N)-2):
    L = i + 1
    R = len(N) - 1

    while (L < R):
      if N[i] + N[L] + N[R] == target:
        print N[i], N[L],   N[R]
        return True
      elif N[i] + N[L] + N[R] < target:
        L = L+1
      elif N[i] + N[L] + N[R] > target:
        R = R-1

def main():
	n = [1,2,3,4,5,6]
	print better_triplets(n, 12)

if __name__ == '__main__':
	main()
