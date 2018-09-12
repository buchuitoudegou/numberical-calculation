#from matrix import *
from numpy import *
def gauss_2(matrix, b):
	for i in range(matrix.shape[0]-1):
		matrix = row_change(matrix, i, b)
		for j in range(i+1, matrix.shape[0]):
			m = matrix[j, i] / matrix[i, i]
			for k in range(i, matrix.shape[0]):
				matrix[j, k] = matrix[j, k] - m * matrix[i, k]
			b[j, 0] = b[j, 0] - m * b[i, 0]
	x = []
	for i in range(matrix.shape[0]):
		x.append(0)
	x[matrix.shape[0] - 1] = b[matrix.shape[0] - 1, 0] \
	 / matrix[matrix.shape[0] -1, matrix.shape[0] -1]
	#print(x[2])
	for i in reversed(range(matrix.shape[0] - 1)):
		sum1 = 0
		for j in range(i + 1, matrix.shape[0]):
			sum1 += matrix[i, j] * x[j]
		tmp = (b[i, 0] - sum1) / matrix[i, i]
		x[i] = tmp;
	result = mat(x)
	return result.T

def row_change(matrix, i, b):
	index = -1
	max_num = matrix[i,i]
	for j in range(i+1, matrix.shape[0]):
		if abs(matrix[j, i]) > abs(max_num):
			index = j
			max_num = matrix[j, i]
	if index != -1:
		matrix[[i,index]] = matrix[[index,i]]
		b[[i,index]] = b[[index, i]]
	return matrix;