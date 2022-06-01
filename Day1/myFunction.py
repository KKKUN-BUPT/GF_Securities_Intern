import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# 空函数
def nop():
    pass


# 坐标转换函数
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


# 解方程函数
def quadratic(a, b, c):
    if not isinstance(a * b * c, (int, float)):
        raise TypeError('bad operand type')
    delta = b * b - 4.0 * a * c
    print(delta)
    if delta < 0:
        return
    x1 = 0.0
    x2 = 0.0
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    if delta == 0:
        return x1
    if delta > 0:
        x2 = (-b - math.sqrt(delta)) / (2 * a)
    return x1, x2


# 乘积计算函数
def mul(x, *args):
    res = x
    for i in args:
        res *= i
    return res


# 汉诺塔
def moveHanoiTower(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        moveHanoiTower(n - 1, a, c, b)  # 将除了最下面的一个移动到b

        print(a, '-->', c)  # 将最下面的一个移动到c

        moveHanoiTower(n - 1, b, a, c)  # 递归还未移动到c的盘子
