from numpy import *
import math

# 一次插值
def linear_interpolation(coord, x):
    k = (coord[1]['y'] - coord[0]['y']) / (coord[1]['x'] - coord[0]['x'])
    return coord[0]['y'] + k * (x - coord[0]['x'])

# 二次插值
def quadratic_interpolation(coord, x):
    k1 = coord[0]['y'] * (x - coord[1]['x']) * (x - coord[2]['x']) / \
    (coord[0]['x'] - coord[1]['x']) / (coord[0]['x'] - coord[2]['x'])
    k2 = coord[1]['y'] * (x - coord[0]['x']) * (x - coord[2]['x']) / \
    (coord[1]['x'] - coord[0]['x']) / (coord[1]['x'] - coord[2]['x'])
    k3 = coord[2]['y'] * (x - coord[0]['x']) * (x - coord[1]['x']) / \
    (coord[2]['x'] - coord[0]['x']) / (coord[2]['x'] - coord[1]['x'])
    return k1 + k2 + k3

# 三次插值
def cubic_interpolation(coord, x):
    _sum = 0
    for i in range(4):
        temp = coord[i]['y']
        product = 1
        merchant = 1
        for j in range(4):
            if j != i:
                product *= x - coord[j]['x']
                merchant *= coord[i]['x'] - coord[j]['x']
        temp = temp * product / merchant
        _sum += temp
    return _sum


# test
if __name__ == "__main__":
    print('一次插值: ', end=' ')
    print(linear_interpolation(\
        [{'x': 0.34, 'y': 0.333487}, {'x': 0.36, 'y': 0.352274}], 0.35))
    print('二次插值: ', end=' ')
    print(quadratic_interpolation(\
        [{'x': 0.32, 'y': 0.314567}, {'x': 0.34, 'y': 0.333487}, \
        {'x': 0.36, 'y': 0.352274}],0.35))
    print('三次插值: ', end=' ')
    print(cubic_interpolation(\
    [{'x': 0.32, 'y': 0.314567}, {'x': 0.34, 'y': 0.333487}, \
        {'x': 0.36, 'y': 0.352274}, {'x': 0.38, 'y': 0.370920}],0.35))
    print('结果: ', end=' ')
    print(math.sin(0.35))
