from numpy import *
from scipy.linalg import orth
from scipy.linalg import solve
import random
from iteration import *
from m import *
import numpy as np
import warnings 
import matplotlib.pyplot as plt
import time
warnings.filterwarnings('error')  

def sec_norm(v):
	sum1 = 0
	for i in range(v.shape[0]):
		try:
			sum1 += v[i,0] ** 2
		except Warning as e:
			#sum1 += v[i,0]
			#print(v[i,0])
			pass
	return sqrt(sum1)

def test(n,test_function):
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
	b1 = b.getA()
	m = np.array(m)
	b1 = np.array(b1)
	x = mat(solve(m,b1))
	#print(x)
	r = test_function(matrix,b)
	#print(r)
	delta = r - x
	dev = sec_norm(delta) / sec_norm(x)
	print(dev)

if __name__ == "__main__":
	# add code to test any function
	pass