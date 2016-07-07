#n = number of people frenemy is the relationship type 
#x = index of person A 
#y = index of person B relationship 
#

# - F E 
# F - F 
# E F -

#In this example, individual 0 and individual 2 have a relationship chain E (0,2), but they also have the relationship chains FF (0<-->1<-->2) and EFFE (0<-->2<-->1<-->0<-->2) that is cycles of relationships are possible. These relationships have the following properties
#1. Being friends and enemies are symmetric, so if person A is friend with person B that implies that person B is also friends with Person A, similarly with enemies 
#2. A person cannot have a relationship to themself and so no relationshp chain will include 0<-->0 
#3.The only valid relationships are F, E, or - (friend, enemy, or neither) Given a matrix of size n x n, the indices for 2 individuals, and a relationshp chain as a string, return if 1 this relationshp exists between 2 people and 0 if otherwise.

#0<->1

 #the_node, current_index_in_the_relationship_chain_string. The starting state is: start_node, 0
#and the goal state is end_node, relationship_chain_string.size()
import numpy as np

def is_Frenemy(n, frenemy, x, y, relationship): 
	np.matrix(frenemy)
	#enemy_matrix = [[0 for x in range(n)] for x in range(n)]
	
	friend_matrix = [[0 for x in range(n)] for x in range(n)]

	enemy_matrix = np.zeros((n,n))
	friend_matrix = np.zeros((n,n))

	for i in range(n):
		for j in range(n):
			if frenemy[i][j] == 'E':
				enemy_matrix[i][j] = True
				friend_matrix[i][j] = False
			elif frenemy[i][j] == '-':
				enemy_matrix[i][j] = False
				friend_matrix[i][j] = False
			elif frenemy[i][j] == 'F':
				enemy_matrix[i][j] = False
				friend_matrix[i][j] = True
	
	if relationship[0] == 'E':
		path = enemy_matrix
	else:
		path = friend_matrix 

	for i in range(1, len(relationship)):
		if relationship[i] == 'E':
			path = path * np.matrix(enemy_matrix)
		else: 
			path = path * np.matrix(friend_matrix)

	if path[x,y]:
		return 1
	else:
		return 0



def main():
	frenemy_matrix1 = [['-', 'F', 'E'], ['F', '-', 'F'], ['E', 'F', '-']]
	frenemy_matrix2 = [['-', 'F', 'E', 'F'], ['F', '-', 'F' 'F'], ['F', 'F', '-' 'F'], ['F', 'E', 'F', '-']]


	assert is_Frenemy(3, frenemy_matrix1, 0, 2, 'EFFE') == 1
	assert is_Frenemy(3, frenemy_matrix1, 0, 2, 'FF') == 1
	assert is_Frenemy(3, frenemy_matrix1, 0, 2, 'FFF') == 0


if __name__ == '__main__':
	main()
