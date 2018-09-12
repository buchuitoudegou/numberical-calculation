import math
from numpy import *
from sympy import *
def f(x):
    if x == 0:
        return 1
    else:
        return math.sin(x) / x
'''
# 梯形法
# @params {f} 原函数
# @params {from_} 起点
# @params {to_} 终点
# @params {n} 份数
'''
def trapezoid(f, from_, to_, n):
    h = (to_ - from_) / n
    sum_ = 0
    for i in range(1, n):
        sum_ += f(from_ + i * h)
    return h/2 * (f(from_) + sum_ * 2 + f(to_))

'''
# 辛普森
# @params {f} 原函数
# @params {from_} 起点
# @params {to_} 终点
# @params {n} 份数
'''
def simpson(f, from_, to_, n):
    h = (to_ - from_) / n
    sum_1 = 0
    sum_2 = 0
    for i in range(n):
        sum_1 += f(from_ + i * h + 0.5 * h)
    for i in range(1,n):
        sum_2 += f(from_ + i * h)
    return h / 6 * (f(from_) + 4 * sum_1 + sum_2 * 2 + f(to_))

if __name__ == "__main__":
    print('梯形法: ')
    print('n=5: ', end=' ')
    print(trapezoid(f, 0, 1, 5))
    print('n=9: ', end=' ')
    print(trapezoid(f, 0, 1, 9))
    print('n=17: ', end=' ')
    print(trapezoid(f, 0, 1, 17))
    print('n=33: ', end=' ')
    print(trapezoid(f, 0, 1, 33))
    print('------\n辛普森: ')
    print('n=5: ', end=' ')
    print(simpson(f, 0, 1, 5))
    print('n=9: ', end=' ')
    print(simpson(f, 0, 1, 9))
    print('n=17: ', end=' ')
    print(simpson(f, 0, 1, 17))
    print('n=33: ', end=' ')
    print(simpson(f, 0, 1, 33))
    print('-----')
    print('标准解: ', end=' ')
    x = Symbol('x')
    print('%f' % integrate(sin(x)/x, (x, 0, 1)))