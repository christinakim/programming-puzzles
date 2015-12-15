import numpy as np

def read_weep(sections, days):

	s = len(sections)
	d = len(days)

	memo = np.zeros((s + 1, d + 1), dtype=object)
	#base case
	for i in range(s + 1):
		for j in range (d + 1):
			memo[i,j] = 0 

	for m in range(len(days)-1, 0, -1):
		print "this loop"
		for j in range(len(sections)-1,0,-1):
			print "loop 2"
			if (j) is not (s -1) and (m) is not (d -1 ):
				print "here"
				t = 0
				#keeping track of time spent reading 
				for l in range(0, j):
				 	t = sections[l] + t

				sameDay = memo[sections[(j + 1)], days[m]]
				freeTime = max(math.pow((m - t),4), 0) 
				sleepLoss = max((t - m), 0)
				newDay = memo[sections[j + 1], days[m + 1]] + freeTime + sleepLoss
				memo[j,m] = min(sameDay,newDay)


	return memo[s,d]



def main():
	J = [3, 1, 5, 4]
	M = [5, 4, 6]
	print read_weep(J,M)

if __name__ =='__main__':
	main()
