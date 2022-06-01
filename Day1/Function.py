from Day1.myFunction import *

# 调用函数
help(abs)  # 查看某函数的帮助信息，如果没有则返回函数头

# 练习
# 把一个整数转换成十六进制表示的字符串
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))

# 定义函数
print(my_abs(-99))  # 函数定义在my_abs.py，使用前先import

# 空函数
nop()

# 参数检查
# abs("A")
# my_abs("A")

# 返回多个值
x, y = move(100, 100, 60, math.pi / 6)
print(x)
print(y)
r = move(100, 100, 60, math.pi / 6)
print(r)

# 练习
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程的两个解。
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

# 函数的参数
# 练习
# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))

# 递归函数
# 练习：
# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法
moveHanoiTower(3, 'A', 'B', 'C')
