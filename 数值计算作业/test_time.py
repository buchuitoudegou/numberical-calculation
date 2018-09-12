import time
from test import *
from m import *
from iteration import *
from matrix2 import *
import copy
import matplotlib.pyplot as plt
t1_arr = []
t2_arr = []
def test_time(n):
	mu = 0
	sigma = 5
	s=np.random.normal(mu,sigma,100)
	mat_arr = []
	for i in range(n):
		tmp = []
		for j in range(n):
			tmp.append(random.uniform(0, 10.0))
		mat_arr.append(tmp)
	A = mat(mat_arr)
	B = mat(orth(A))
	arr_D = []
	for i in range(n):
		tmp = []
		for j in range(n):
			if not i == j:
				tmp.append(0)
			else:
				tmp.append(random.uniform(0, 1))
		arr_D.append(tmp)
	D = mat(arr_D)
	#print(A)
	matrix = B.I * D * B
	m = matrix.getA()
	b_arr = []
	for i in range(n):
		index = random.randint(0,100)
		b_arr.append([s[index]])
	b = mat(b_arr)
	t1 = time.time()
	jacobi(matrix,b)
	t2 = time.time()
	print("jacobi time: " + str(t2-t1))
	print("-------------------------")
	t1 = time.time()
	gauss_siedel(matrix,b)
	t2 = time.time()
	print("gauss_siedel time: " + str(t2-t1))
	print("-------------------------")
	t1 = time.time()
	SoR_gauss_siedel(matrix,b,1.1)
	t2 = time.time()
	print("SoR time: " + str(t2-t1))
	print("-------------------------")
	t1 = time.time()
	conjugate_gradient(matrix,b)
	t2 = time.time()
	print("conjugate time: " + str(t2-t1))
	print("-------------------------")
	t1 = time.time()
	gauss(copy.copy(matrix), copy.copy(b))
	t2 = time.time()
	t1_arr.append(t2-t1)
	print("gauss time: " + str(t2-t1))
	print("-------------------------")
	t1 = time.time()
	gauss_2(copy.copy(matrix), copy.copy(b))
	t2 = time.time()
	t2_arr.append(t2-t1)
	print("gauss2 time: " + str(t2-t1))


def SoR_test(n):
	mu = 0
	sigma = 5
	s=np.random.normal(mu,sigma,100)
	mat_arr = []
	for i in range(n):
		tmp = []
		for j in range(n):
			tmp.append(random.uniform(0, 10.0))
		mat_arr.append(tmp)
	A = mat(mat_arr)
	B = mat(orth(A))
	arr_D = []
	for i in range(n):
		tmp = []
		for j in range(n):
			if not i == j:
				tmp.append(0)
			else:
				tmp.append(random.uniform(0, 1))
		arr_D.append(tmp)
	D = mat(arr_D)
	matrix = B.I * D * B
	m = matrix.getA()
	b_arr = []
	for i in range(n):
		index = random.randint(0,100)
		b_arr.append([s[index]])
	b = mat(b_arr)
	t1 = time.time()
	SoR_gauss_siedel(matrix,b,1)
	t2 = time.time()
	print("w = 1: " + str(t2-t1))
	print("-------------------------")
	t1 = time.time()
	SoR_gauss_siedel(matrix,b,1.1)
	t2 = time.time()
	print("w = 1.1: " + str(t2-t1))
	print("-------------------------")
	t1 = time.time()
	SoR_gauss_siedel(matrix,b,0.5)
	t2 = time.time()
	print("w = 0.5: " + str(t2-t1))
	print("-------------------------")
	t1 = time.time()
	gauss_siedel(matrix,b)
	t2 = time.time()
	print("gauss_siedel: " + str(t2-t1))
	

# TO DO: TEST TIME
# ADD CODE TO TEST

test_time(10)
test_time(50)
test_time(100)
test_time(200)

plt.figure()
plt.xlabel('n')
plt.ylabel('time')
plt.plot([10,50,100,200], t1_arr,'r--',[10,50,100,200],t2_arr,'h-.')
plt.savefig("./direction.png")

SoR_test(50) 