import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
f = lambda x,y: y-2*x/y

'''
# 前进欧拉
# @params {f} 微分函数
# @params {x0} 初始点
# @params {y0} 初始值
'''
def forward_euler(f, x0, y0):
    x = []
    y = []
    x.append(x0)
    y.append(y0)
    for i in range(10):
        x_new = x[-1] + 0.1
        y_new = y[-1] + 0.1 * f(x[-1], y[-1])
        x.append(x_new)
        y.append(y_new)
    return [x, y]
'''
# 后退欧拉
# @params {f} 微分函数
# @params {x0} 初始点
# @params {y0} 初始值
'''
def backward_euler(f, x0, y0):
    x = [x0]
    y = [y0]
    for i in range(10):
        y_new = iteration(f, x[-1], y[-1])
        x_new = x[-1] + 0.1
        x.append(x_new)
        y.append(y_new)
    return [x, y]

def iteration(f, x0, y0):
    y_new = y0 + 0.1 * f(x0, y0)
    x_new = x0 + 0.1
    for i in range(50):
        y_new = y0 + 0.1 * f(x_new, y_new)
    return y_new
'''
# 梯形法
# @params {f} 微分函数
# @params {x0} 初始点
# @params {y0} 初始值
'''
def trapezoid(f, x0, y0):
    x = [x0]
    y = [y0]
    for i in range(10):
        y_new = y[-1] + 0.1 * f(x0, y0)
        x_new = x[-1] + 0.1
        for j in range(50):
            y_new = y[-1] + 0.05 * (f(x[-1], y[-1]) + f(x_new, y_new))
        x.append(x_new)
        y.append(y_new)
    return [x, y]

'''
# 改进欧拉
# @params {f} 微分函数
# @params {x0} 初始点
# @params {y0} 初始值
'''
def improve_euler(f, x0, y0):
    x = [x0]
    y = [y0]
    for i in range(10):
        x_new = x[-1] + 0.1
        yp = y[-1] + 0.1 * f(x[-1], y[-1])
        yc = y[-1] + 0.1 * f(x_new, yp)
        y_new = 0.5 * (yp + yc)
        x.append(x_new)
        y.append(y_new)
    return [x, y]

def diff_equation(y,x):
    return np.array(y-2*x/y)
if __name__ == "__main__":
    x, y = forward_euler(f, 0, 1)[0], forward_euler(f, 0 ,1)[1]
    x1, y1 = backward_euler(f, 0, 1)[0], backward_euler(f, 0, 1)[1]
    x2, y2 = trapezoid(f, 0, 1)[0], trapezoid(f, 0, 1)[1]
    x3, y3 = improve_euler(f, 0 , 1)[0], improve_euler(f, 0 , 1)[1]
    fig = plt.figure()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x, y, color='green')
    plt.plot(x1, y1, color='red')
    plt.plot(x2, y2, color='blue', marker='_')
    plt.plot(x3, y3, color='cyan', marker='x')
    x=np.linspace(0,1,num=100)
    result=odeint(diff_equation,1,x)
    plt.plot(x,result[:,0], color='magenta')
    plt.savefig('../assets/ordinary-diff.png')