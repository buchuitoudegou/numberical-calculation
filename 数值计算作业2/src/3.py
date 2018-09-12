import numpy as np 
from numpy import *
import random
from scipy.linalg import solve
import matplotlib.pyplot as plt
import math
np.seterr(divide='ignore', invalid='ignore')
def generate():
    A = []
    b = []
    I = []
    p = []
    mu = 0
    sigma = 5
    s = np.random.normal(mu, sigma, 120000)
    for i in range(10000):
        A.append([])
        for j in range(10):
            A[-1].append(s[random.randint(0, 119999)])
        b.append([s[random.randint(0, 119999)]])
    for i in range(10):
        I.append([])
        p.append([])
        for j in range(10):
            if i == j:
                I[-1].append(1)
                p[-1].append(10000)
            else:
                I[-1].append(0)
                p[-1].append(0)
    return [A, b, I, p]

def least_square(A, b, I, p, x_s):
    x0 = []
    for i in range(10):
        x0.append([random.randint(1,10)])
    x0 = mat(x0)
    x = [x0]
    error = []
    steps = []
    for i in range(10000):
        q = p * A[i].T / (1 + A[i] * p * A[i].T)
        x.append(x[-1] + q * (b[i,0] - A[i] * x[-1]))
        p = (I - q * A[i]) * p
        error.append(norm(x[-1], x_s))
        if len(steps) > 0:
            steps.append(steps[-1] + 1)
        else:
            steps.append(1)
    print(error[1000])
    plt.figure()
    plt.plot(steps[:100], error[:100])
    plt.savefig('../assets/least_square.png')

def norm(x, y):
    sum_ = 0
    for i in range(10):
        sum_ += (x[i, 0] - y[i, 0]) ** 2
    return math.sqrt(sum_)

if __name__ == "__main__":
    l = generate()
    A, b, I, p = l[0], l[1], l[2], l[3]
    A = mat(A)
    b = mat(b)
    x_s = solve(array(A.T * A), array(A.T * b))
    least_square(A, b, I, p, mat(x_s))