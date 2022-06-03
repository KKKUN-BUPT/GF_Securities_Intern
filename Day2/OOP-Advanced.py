# __slot__
from enum import Enum, unique
from types import MethodType


class Student(object):
    pass


s = Student()
# 可以给对象实例绑定属性或者方法，但是效果仅限于本实例
# 如果需要所有实例可用，需要绑定在class中
s.name = 'Michael'  # 绑定属性


def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


s.set_age = MethodType(set_age, s)


# 给类绑定方法
def set_score(self, score):
    self.score = score


Student.set_score = set_score


# 通过slot限制该类的实例可以绑定的属性
# 但是__slot__只作用于该类，子类不会主动继承，除非在子类中也定义了__slot__
class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


s = Student()  # 创建新的实例
try:
    s.score = 99  # 绑定属性'score'
except AttributeError as e:
    print('AttributeError:', e)


# @property
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    # 注意！方法名不能和实例变量名重复！否则会出现递归死循环导致栈溢出！
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth


# 练习
# 利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be an integer!')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be an integer!')
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')


# 多重继承
# python允许多继承，为了更好的看出继承关系，可以将非主要继承类命名为xxxMixIn，这些MixIn的意义和Java中的接口类似，里面的方法不是抽象方法


# 定制类
# 相当于对方法执行时内部调用的一些方法进行重写

class Student(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__


print(Student('Michael'))


class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a


for n in Fib():
    print(n)


class Fib(object):

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


f = Fib()
print(f[0])
print(f[5])
print(f[100])
print(f[0:5])
print(f[:10])


class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


s = Student()
print(s.name)
print(s.score)
print(s.age())


# print(s.grade)


class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


s = Student('Michael')
s()

# 枚举类

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


# 练习
# 把Student的gender属性改造为枚举类型，可以避免使用字符串
@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')


# 使用元类
def fn(self, name='world'):
    print('Hello, %s.' % name)


Hello = type('Hello', (object,), dict(hello=fn))

h = Hello()
print('call h.hello():')
h.hello()
print('type(Hello) =', type(Hello))
print('type(h) =', type(h))


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


# 指示使用ListMetaclass来定制类
class MyList(list, metaclass=ListMetaclass):
    pass


L = MyList()
L.add(1)
L.add(2)
L.add(3)
L.add('END')
print(L)


class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


# testing code:

class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()
