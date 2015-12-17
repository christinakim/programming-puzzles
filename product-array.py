"""
input [2,3,4]
output [12, 8, 6] = [3*4, 2*4, 2*3]
"""
def product(n):
	total = 1
	output = []
	count = 0

	if len(n)==1:
		return [0]
	for i in range(len(n)):
		if n[i] != 0:
			total = n[i] * total
		else: 
			count = count + 1

	for i in range(len(n)):
		if n[i] == 0 and count ==1:
			output.append(total)
		elif count == 1:
			output.append(0)
		elif count >1:
			output.append(0)
		else: 
			output.append(total/n[i])

	return output