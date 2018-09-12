from numpy import *
from decimal import *
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import math
import time
def equals(a, b):
    return Decimal(a).quantize(Decimal('0.000000')) ==\
    Decimal(b).quantize(Decimal('0.000000'))

def digit_judgement(a):
    string = str(a)
    i = string.index('.')
    if (len(string) - i - 1 >= 6):
        return True
    else:
        return False
def draw(x, y, name, num):
    plt.figure(num)
    #ax = plt.subplot(200+num)
    #ax.xaxis.set_major_locator(MultipleLocator(0.01))
    print(x)
    plt.plot(x, y)
    plt.savefig('../assets/'+ name + '-time.png')
# 二分法
def dichotomy(f, x1, x2):
    current = (x1 + x2) / 2
    count = [0]
    Time = [0]
    begin = time.time()
    errors = [abs(current-math.sqrt(115)) / math.sqrt(115)]
    while(True):
        if f(current) < 0:
            x1 = current
        elif f(current) > 0:
            x2 = current
        else:
            return current
        if equals(f(current), 0):
            break
        current = (x1 + x2) / 2
        count.append(count[-1] + 1)
        time.sleep(0.1)
        Time.append(time.time())
        errors.append(abs(current - math.sqrt(115))/ math.sqrt(115))
    plt.figure(1)
    ax = plt.subplot(111)
    ax.yaxis.set_major_locator(MultipleLocator(0.01))
    plt.ylim(0,0.05)
    plt.plot(count, errors)
    plt.savefig('../assets/dichotomy.png')
    draw(Time, errors, 'dichotomy', 11)
    return current

'''
# 牛顿法 
# @params {f} 原函数
# @params {f_} 原函数的导数
# @params {x} 初始值
'''
def newton(f, f_, x):
    count = [0]
    errors = [abs(x - math.sqrt(115)) / math.sqrt(115)]
    Time = [time.time()]
    while(True):
        x1 = x - f(x) / f_(x)
        if equals(x1, x):
            x = x1
            break
        else:
            x = x1
        count.append(count[-1] + 1)
        errors.append(abs((x - math.sqrt(115)))/ math.sqrt(115))
        time.sleep(0.1)
        Time.append(time.time())
    plt.figure(2)
    ax = plt.subplot(121)
    ax.yaxis.set_major_locator(MultipleLocator(0.01))
    plt.ylim(0,0.05)
    plt.plot(count, errors)
    plt.savefig('../assets/newton.png')
    draw(Time, errors, 'newton', 12)
    return x 

'''
# 简化牛顿法
# @params {f} 原函数
# @params {f_x} 原函数在起始点的梯度
# @params {x} 起始点
'''
def simple_newton(f, f_x, x):
    count = [0]
    errors = [abs(x - math.sqrt(115)) / math.sqrt(115)]
    Time = [time.time()]
    while(True):
        x1 = x - f(x) / f_x
        if equals(x1, x):
            x = x1
            break
        else:
            x = x1
        count.append(count[-1] + 1)
        errors.append(abs((x - math.sqrt(115)))/ math.sqrt(115))
        time.sleep(0.1)
        Time.append(time.time())
    plt.figure(3)
    ax = plt.subplot(191)
    ax.yaxis.set_major_locator(MultipleLocator(0.01))
    plt.ylim(0,0.05)
    plt.plot(count, errors)
    plt.savefig('../assets/simple-newton.png')
    draw(Time, errors, 'simplenewton', 13)
    return x

'''
# 弦截法
# @params {f} 原函数
# @params {x0} 近似根1
# @params {x1} 近似根2
'''
def secant(f, x0, x1):
    count = [0]
    errors = [abs(x1 - math.sqrt(115)) / math.sqrt(115)]
    Time = [time.time()]
    while(True):
        x_new = x1 - f(x1) / (f(x1) - f(x0)) * (x1 - x0)
        if equals(x_new, x1):
            x1 = x_new
            break
        else:
            x0 = x1
            x1 = x_new
        count.append(count[-1] + 1)
        errors.append(abs((x1 - math.sqrt(115)))/ math.sqrt(115))
        time.sleep(0.1)
        Time.append(time.time())
    plt.figure(4)
    plt.ylim(0,0.05)
    plt.plot(count, errors)
    plt.savefig('../assets/secant.png')
    draw(Time, errors, 'secant', 14)
    return x1


if __name__ == '__main__':
    print('二分法: ', end=' ')
    print('%.6f' % dichotomy(lambda x: x ** 2 - 115, 10, 11))
    print('牛顿法: ', end=' ')
    print('%.6f' % newton(lambda x: x ** 2 - 115, lambda x: 2*x, 10))
    print('简化牛顿法: ', end=' ')
    print('%.6f' % simple_newton(lambda x: x ** 2 - 115, 20, 10))
    print('弦截法: ', end=' ')
    print('%.6f' % secant(lambda x: x ** 2 - 115, 10, 11))
    