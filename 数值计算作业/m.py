from numpy import *
from matrix2 import *
def input_matrix():
	n = int(input("input the size of a n*n matrix: "))
	matarr = []
	for j in range(n):
		string = input()
		string = string.split(" ")
		for i in range(len(string)):
			string[i] = float(string[i])
		#print(string)
		matarr.append(string)
	matrix = mat(matarr)
	return matrix

def input_vector():
	n = int(input("size of the vector: "))
	matarr = []
	for i in range(n):
		arr = []
		arr.append(float(input()))
		matarr.append(arr)
	#print(matarr)
	v = mat(matarr)
	return v

def gauss(matrix, b):
	for i in range(matrix.shape[0]-1):
		for j in range(i+1, matrix.shape[0]):
			m = matrix[j, i] / matrix[i, i]
			#print(m)
			for k in range(i, matrix.shape[0]):
				matrix[j, k] = matrix[j, k] - m * matrix[i, k]
			b[j, 0] = b[j, 0] - m * b[i, 0]
			#print(matrix)
	#print(b)
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

if __name__ == "__main__":
	#m = input_matrix()
	#print(m)
	m = mat([[1.0,1.0,1.0],[0.0,4.0,-1.0],[2.0,-2.0,1.0]])

	b = mat([[6.0],[5.0],[1.0]])
	print(b)
	#b = input_vector()
	#print(b)
	r = gauss_2(m,b)
	print(r)