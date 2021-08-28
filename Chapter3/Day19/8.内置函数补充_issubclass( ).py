'''判断类是否是某个类的子孙类'''


class Foo(object):
    pass


class Base(Foo):
    pass


class Top(Base):
    pass


print(issubclass(Foo, Base))  # F
print(issubclass(Top, Base))  # T
print(issubclass(Foo, object))  # T
