w = 6
matrix = []

matrix  = [[0, 3, 5, 7, 2, 4, 5, 7, 9, 1, 1, 2], \
		   [1,0,5,6,9,2,5,0,7,1,1,2], \
		   [3,5,0,3,0,4,5,3,6,2,3,1], \
		   [3,6,3,0,3,1,2,3,4,3,5,8], \
		   [4,2,8,10,0,2,5,6,7,2,2,3], \
		   [2,8,1,0,2,0,4,5,6,1,2,3], \
		   [2, 8,1,0,2,5,0,6,7,1,2,3], \
		   [3,4,3,6,2,1,1,0,5,0,0,0], \
		   [5,3,5,5,3,6,2,2,0,1,2,4], \
		   [5, 3, 1, 1, 1, 6, 2, 2, 0, 0, 2, 4], \
		   [5, 3, 0, 0, 0, 0, 0, 2, 0, 1, 0, 4], \
		   [5, 3, 1, 1, 1, 2, 2, 2, 0, 1, 2, 0]]

def getWeight(nodei):
		global matrix
		print "*******************"
		print nodei
		sum =0
		# for i in range(0,w):
		# 	for j in range(0,w):
		# 		sum = sum + Matrix[i][j] + Matrix[j][i]
		for i in range(0,w):
			sum += matrix[int(nodei)][i]
			sum += matrix[i][int(nodei)]
		return sum


# for i in range(0,5):
# 	entry = []
# 	Matrix.append(entry)


# Matrix[0].append() 0
# Matrix[0][1] = 3
# Matrix[0][2] = 5
# Matrix[0][3] = 7
# Matrix[0][4] = 2
# Matrix[1][0] = 1
# Matrix[1][1] = 0
# Matrix[1][2] = 4
# Matrix[1][3] = 9
# Matrix[1][4] = 4
# Matrix[2][0] = 7
# Matrix[2][1] = 1
# Matrix[2][2] = 0
# Matrix[2][3] = 4
# Matrix[2][4] = 5
# Matrix[3][0] = 2
# Matrix[3][1] = 3
# Matrix[3][2] = 8
# Matrix[3][3] = 0
# Matrix[3][4] = 6
# Matrix[4][0] = 7
# Matrix[4][1] = 3
# Matrix[4][2] = 2
# Matrix[4][3] = 1
# Matrix[4][4] = 0
