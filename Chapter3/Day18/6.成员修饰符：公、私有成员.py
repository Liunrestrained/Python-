import self as self


class Foo(object):

    def __init__(self, name, age):
        self.__name = name  # 私有成员__，只允许在类中调用,被继承的类的私有成员也只能在自己的类中调用。
        self.age = age

    def get_data(self):
        return self.__name

    def get_age(self):
        return self.age


obj = Foo("树人", 33)

# 公有成员
print(obj.age)
# v1 = self.get_age()  # 错误示范
v1 = obj.get_age()
print(v1)

# 私有成员
# print(obj.__name)  # 不允许外界直接访问获取
v2 = obj.get_data()
print(v2)
