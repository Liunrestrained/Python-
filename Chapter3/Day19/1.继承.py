'''继承的意义：将公共的方法提取到父类，增加代码的重复使用用性'''
'''调用类中的成员时：有限在自己的类中寻找，没有则到自己继承的父类中寻找，多继承的情况下，先找左边，再找右边。
详细完整的查找法需要使用mro()函数和c3算法。'''


# 编写方式：
# 简单的继承：
class Foo(object):
    print(1)


class Base(Foo):
    print(2)


# 多继承：
class Apple(object):
    print(1)


class Angel(object):
    print(2)


class China(Apple, Angel):
    print(3)
