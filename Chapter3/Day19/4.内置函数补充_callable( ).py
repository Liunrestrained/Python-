'''callable，判断是否可以在后面加括号执行？'''


# 1.函数
def func():
    pass


print(callable(func))  # True


# 2.类
class Foo(object):
    pass


print(callable(Foo))  # True


# 类中具有__call__方法的对象
class BBA(object):
    pass


obj = BBA()
print(callable(obj))  # False


class Tnt(object):

    def __call__(self, *args, **kwargs):
        pass


obj = Tnt()
print(callable(obj))  # True
