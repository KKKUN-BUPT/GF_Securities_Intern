# 切片
L = list(range(100))
# [ : ] 冒号前是起始值(不写表示从头开始)，冒号后是个数（不写表示到最后位置）
# [ : : ] 第二个冒号后是间隔值
# 负数表示从后往前数
print(L[:10])
print(L[-10:])
print(L[10:20])
print(L[:10:2])
print(L[::5])


# print(L[:])


# 练习
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格
def trim(s):
    if s == '':
        return s
    while len(s) > 0 and s[:1] == ' ':
        s = s[1:]
    while len(s) > 0 and s[-1] == ' ':
        s = s[:-1]
    return s


print(trim('hello  '))
print(trim('  hello'))
print(trim('  hello  '))
print(trim('  hello  world  '))
print(trim(''))
print(trim('    '))


# 迭代
# 练习
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L):
    if not L:
        return None, None
    my_min = L[0]
    my_max = L[0]
    for i in L:
        my_min = min(my_min, i)
        my_max = max(my_max, i)
    return my_min, my_max


if findMinAndMax([]) != (None, None):
    print('测试失败1!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败2!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败3!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败4!')
else:
    print('测试成功!')

# 列表生成式
# 练习
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')


# 生成器
# 练习
# 输出杨辉三角
def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[n] + L[n + 1] for n in range(len(L) - 1)] + [1]


n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)
