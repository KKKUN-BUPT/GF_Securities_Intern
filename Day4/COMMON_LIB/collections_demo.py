from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import Counter

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print('Point:', p.x, p.y)

Circle = namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(0, 0, 1)
print("circle:", c.x, c.y, c.r)

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

# 类似与javaHashMap中的getOrDefault方法
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print('dd[\'key1\'] =', dd['key1'])
print('dd[\'key2\'] =', dd['key2'])

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
