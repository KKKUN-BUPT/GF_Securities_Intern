# 高阶函数
# map/reduce
# 练习
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
import functools
import time
from functools import reduce


def normalize(name):
    name = name[0].upper() + name[1:].lower()
    return name


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(L):
    def f(x, y):
        return x * y

    return reduce(f, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 利用map和reduce编写一个str2float函数
def str2float(s):
    def fn1(x, y):
        return x * 10 + y

    def char2num(s):
        DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return DIGITS[s]

    L = s.split('.')
    return reduce(fn1, map(char2num, L[0])) + reduce(fn1, map(char2num, L[1])) / 10 ** len(L[1])


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


# filter
# 练习
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数
def is_palindrome(n):
    return str(n) == str(n)[::-1]  # [::-1]表示反转字符串


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
                                                  111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

# sorted
# 练习
# 请用sorted()对列表按名字排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


L2 = sorted(L, key=by_name)
print(L2)


# 请用sorted()对列表按成绩从高到低排序
def by_score(t):
    return t[1]


L2 = sorted(L, key=by_score, reverse=True)
print(L2)


# 返回函数
# 练习
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    x = 0

    def counter():
        nonlocal x  # 将x声明为非局部变量，即视作外层函数的局部变量

        x = x + 1
        return x

    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


# 匿名函数
# 练习
# 请用匿名函数改造下面的代码
def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))
print(L)

L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L)


# 装饰器
# 练习
# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
def metric(fn):
    @functools.wraps(fn)
    # *args, **kw用于接收任何参数
    def decorator(*args, **kw):
        t1 = time.time()
        res = fn(*args, **kw)
        print('%s executed in %s ms' % (fn.__name__, (time.time() - t1) * 1000))
        return res

    return decorator


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
print(f)
s = slow(11, 22, 33)
print(s)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试通过!')


# 偏函数 Partial function
# 总结
# functools.partial的作用是将一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
