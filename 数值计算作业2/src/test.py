import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
#一阶微分方程的例子
def diff_equation(y,x):
    return np.array(y-2*x/y)#微分方程格式，左边一定是dy/dx,返回右边
x=np.linspace(0,1,num=100)#初始点是0
result=odeint(diff_equation,1,x)#中间那个是y0初值，即x=0时y=1
plt.plot(x,result[:,0])#result整个矩阵的第一列
plt.show()