'''迭代器的定义：
1.当类中定义了__iter__和__next__两个方法；
2.__iter__方法需要返回对象本身，即：self
3.__next__方法，返回下一个数据，如果没有数据了，则需需要抛出一个StopIteration的异常
官方文档：https://docs.python.org/3/library/stdtypes.html#iterator-types'''


# 创建迭代器类型：
class IT(object):
    def __init__(self):
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter == 3:
            raise StopIteration()
        return self.counter


# 根据类，实例化创建一个迭代器对象：
obj1 = IT()

v1 = next(obj1)  # next是Python的内置函数，此处相当于obj1.__next__()
print(v1)

v2 = next(obj1)
print(v2)

v3 = next(obj1)
print(v2)

obj2 = IT()
for item in obj2:
    print(item)

# 迭代器对象支持通过next取值，如果取值结束自动抛出StopIteration的异常。
# for循环内部在循环时，先执行__iter__方法，获取一个迭代器对象，然后不断地执行next取值，遇到StopIteration则终止循环。
