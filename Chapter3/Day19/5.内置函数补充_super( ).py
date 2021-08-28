'''按照mro继承关系向上找成员'''


class Top(object):
    def message(self, num):
        print("Top.message", num)


class Base(Top):
    pass


class Foo(Base):

    def message(self, num):
        print("Top.message", num)
        super().message(num + 100)  # 根据继承关系，去继承的所有关系中寻找所有相同的方法，并将将参数传递过去。


obj = Foo()
obj.message(1)

# >>> Top.message 1
# >>> Top.message 101


'''class Base(object):

    def message(self, num):
        print("Base.message", num)
        super().message(1000)


class Bar(object):

    def message(self, num):
        print("Bar.message", num)


class Foo(Base, Bar):
    pass


obj = Foo()
obj.message(1)

>>> Base.message 1
>>> Bar.message 1000'''
