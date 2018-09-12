from numpy import *
from decimal import *
def jacobi(matrix, b):

	print("jacobi iteration : ")

	# create the diagonal matrix of A
	D = diagonal(matrix)
	x0_arr = []
	i_arr = []
	# create identity matrix
	for i in range(matrix.shape[0]):
		tmp = []
		for j in range(matrix.shape[0]):
			if not i == j:
				tmp.append(0)
			else:
				tmp.append(1)
		i_arr.append(tmp)
	i_mat = mat(i_arr)
	# create x0 vector
	for i in range(matrix.shape[0]):
		x0_arr.append([0])
	x0 = mat(x0_arr)
	x_arr = []
	x_arr.append(x0)
	# create f , B matrix
	f = D.I * b
	B = i_mat - D.I * matrix
	count = 0
	# jacobi iteration
	for j in range(502):
		new_x = B * x_arr[j] + f
		count += 1
		if equals(new_x, x_arr[j]):
			break
		x_arr.append(new_x)
	print("jacobi convergence: "+str(count))
	return x_arr[-1]

def diagonal(matrix):
	mat_arr = []
	for i in range(matrix.shape[0]):
		tmp = []
		for j in range(matrix.shape[0]):
			if not i == j:
				tmp.append(0)
			else:
				tmp.append(matrix[i,j])
		mat_arr.append(tmp)
	new_d_matrix = mat(mat_arr)
	return new_d_matrix

def gauss_siedel(matrix, b):
	print("gauss_siedel iteration : ")
	D = diagonal(matrix)
	L = get_L(matrix)
	U = get_U(matrix)
	x0_arr = []
	for i in range(matrix.shape[0]):
		x0_arr.append([0])
	x0 = mat(x0_arr)
	x_arr = []
	x_arr.append(x0)
	count = 0
	for i in range(502):
		new_x = (D - L).I * U * x_arr[i] + (D - L).I * b
		if equals(new_x, x_arr[i]):
			break
		x_arr.append(new_x)
		count += 1
	print("gauss_siedel convergence : " + str(count))
	return x_arr[-1]

def get_U(matrix):
	mat_arr = []
	for i in range(matrix.shape[0]):
		tmp = []
		for j in range(matrix.shape[0]):
			if j > i:
				tmp.append(-matrix[i,j])
			else:
				tmp.append(0)
		mat_arr.append(tmp)
	return mat(mat_arr)

def get_L(matrix):
	mat_arr = []
	for i in range(matrix.shape[0]):
		tmp = []
		for j in range(matrix.shape[0]):
			if j < i:
				tmp.append(-matrix[i,j])
			else:
				tmp.append(0)
		mat_arr.append(tmp)
	return mat(mat_arr)

def SoR_gauss_siedel(matrix, b, w):
	D = diagonal(matrix)
	L = get_L(matrix)
	U = get_U(matrix)
	print("SoR iteration: ")
	x0_arr = []
	for i in range(matrix.shape[0]):
		x0_arr.append([0])
	x0 = mat(x0_arr)
	x_arr = []
	x_arr.append(x0)
	count = 0
	for i in range(501):
		new_x = (D - w * L).I * ((1 - w) * D + w *U) * x_arr[i] + w * (D - w * L).I * b
		if equals(new_x, x_arr[i]):
			break
		x_arr.append(new_x)
		count += 1
	#if count != 4000:
	print("SoR_gauss_siedel convergence with w = " + str(w) + " \
count:"+str(count))
	#else:
	#print("SoR_gauss_siedel not convergence with w = "+ str(w))
	return x_arr[-1]

def conjugate_gradient(matrix, b):
	print("conjugate_gradient iteration: ")
	x0_arr = []
	for i in range(matrix.shape[0]):
		x0_arr.append([0])
	x0 = mat(x0_arr)
	p = r = b - matrix * x0
	x_arr = []
	x_arr.append(x0)
	count = 0
	for i in range(b.shape[0]):
		if equals_zero(r):
			break
		if product(p, matrix * p) == 0:
			break
		temp_a0 = product(r, r) / product(matrix * p, p)
		new_x = x_arr[i] + temp_a0 * p
		r1 = r - temp_a0 * matrix * p
		temp_b0 = product(r1, r1) / product(r, r)
		p = r1 + temp_b0 * p
		r = r1
		if equals(new_x, x_arr[i]):
			break
		x_arr.append(new_x)
		count += 1
	print("conjugate_gradient convergence: " + str(count))
	return x_arr[-1]

def product(v1, v2):
	sum1 = 0.0
	for i in range(v1.shape[0]):
		sum1 += v1[i, 0] * v2[i, 0]
	return sum1

def equals_zero(v):
	for i in range(v.shape[0]):
		if v[i, 0] != 0:
			return False
	return True

def equals(v1, v2):
	try:
		for i in range(v1.shape[0]):
			if Decimal(float(v1[i,0])).quantize(Decimal('0.000')) != Decimal(float(v2[i,0])).quantize(Decimal('0.000')):
				return False
		return True
	except:
		return False

if __name__ == "__main__":
	m = mat([[8.0,-3.0,2.0],[4.0,11.0,-1.0],[6.0,3.0,12.0]])
	#d = diagonal(m)
	b = mat([[20.0],[33.0],[36.0]])
	#m = mat([[3.0,1.0],[1.0,2.0]])
	#b = mat([[5],[5]])
	#r = gauss_siedel(m,b)
	#print(r[-1])
	r = conjugate_gradient(m,b)
	print(r)