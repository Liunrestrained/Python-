'''判断对象是否是某个类，或其子类的实例'''


class Foo(object):
    pass


class Base(Foo):
    pass


class To(Base):
    pass


v1 = Foo()
print(isinstance(v1, Foo))
print(isinstance(v1, Base))
print(isinstance(v1, To))


'''class Animal(object):
    def run(self):
        print("开始执行")


class Dog(Animal):
    print("dog")


class Cat(Animal):
    print("cat")


data_list = [
    "alex",
    Dog(),
    Cat(),
    "root"
]

for item in data_list:
    if type(item) == Cat:
        item.run()
    elif type(item) == Dog:
        item.run()
    else:
        pass

for item in data_list:
    if isinstance(item, Animal):
        item.run()
    else:
        pass
'''