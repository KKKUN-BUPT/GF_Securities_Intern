# 类和实例
import types


class Student(object):

    # __init__方法第一个参数一定是self，但是传参时不需要传入self，因为self代表创建的实例本身=
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
print(lisa.name, ":", lisa.get_grade())
print(bart.name, ":", bart.get_grade())


# 访问限制
# 类似于Java中使用private修饰属性，用get和set方法来操作属性
# python中属性前面加上__表示该变量为私有变量
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def set_name(self, name):
        if name is not None:
            self.__name = name
        else:
            raise ValueError('name is None')


# 练习
# 请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性
class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender == 'male' or 'female':
            self.__gender = gender
        else:
            raise ValueError('invalid gender')


bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')


# 继承和多态
# 父类
class Animal(object):
    def run(self):
        print('Animal is running...')


# 子类
class Dog(Animal):
    pass


class Cat(Animal):
    pass


# 子类可以继承父类的所有方法
dog = Dog()
dog.run()

cat = Cat()
cat.run()


# 子类可以重写父类的方法或者增加自己的方法
class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):

    def run(self):
        print('Cat is running...')


dog = Dog()
dog.run()

cat = Cat()
cat.run()

# isinstance方法判断的是该实例是否属于该类或该类的子类
c = Dog()  # c是Dog类型
print(isinstance(c, Dog))
print(isinstance(c, Animal))

# 获取对象信息
print(type(123))
# 判断对象类型
print(type((x for x in range(10))) == types.GeneratorType)
# 获取对象的所有属性和方法
print(dir('ABC'))


# 判断对象是否有该属性
class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


# 创建对象实例
obj = MyObject()
# 判断是否有属性x
print(hasattr(obj, 'x'))
# 判断是否有属性y
print(hasattr(obj, 'y'))
# 为对象设置一个属性
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))


# 实例属性和类属性
# 即Java中的成员变量和静态变量
class Student(object):
    name = 'Student'

    def __init__(self, name):
        self.name = name


# 创建对象实例
s = Student(None)
# 因为此时没有初始化实例属性name，所以打印的是类属性
print(s.name)
# 这样直接返回的是类属性
print(Student.name)
# 初始化实例属性name后，就无法通过实例对象获取类属性
s.name = 'Michael'
print(s.name)
print(Student.name)


# Python中千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

# 练习
# 为了统计学生人数，请给Student类增加一个类属性，每创建一个实例，该属性自动增加
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
