'''class Foo:
# 基于装饰器编写
    @property
    def x(self):
        print(123)

    @x.setter
    def x(self, value):
        print(value)

    @x.deleter
    def x(self):
        print(789)


obj = Foo()
obj.x
obj.x = 234
del obj.x'''


class C(object):
    '''基于定义变量'''

    def ddd(self):
        print(123)

    def fff(self, value):
        print(value)

    def ggg(self):
        print(567)

    x = property(ddd, fff, ggg, "I'm the 'x' property.")  # 后面是一段解释，前面的不需要可以输入None


obj = C()

obj.x
obj.x = 345
del obj.x


