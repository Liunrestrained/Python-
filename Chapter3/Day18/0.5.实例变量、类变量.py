class Person(object):
    country = "中国"  # 类变量，属于类，可以被所有对象共享，一般用于给对象提供公共数据（类似于全局变量）。

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        # message = "{}-{}-{}".format(Person.country, self.name, self.age)
        message = "{}-{}-{}".format(self.country, self.name, self.age)
        print(message)


print(Person.country)  # 中国

p1 = Person("武沛齐", 20)  # 实例变量，属于对象，每个对象中各自维护自己的数据。
print(p1.name)
print(p1.age)
print(p1.country)  # 中国

p1.show()  # 中国-武沛齐-20
