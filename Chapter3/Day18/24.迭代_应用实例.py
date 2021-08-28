class IT(object):  # 迭代器类型
    def __init__(self):
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter == 3:
            return StopIteration()
        return self.counter


class Foo(object):
    def __iter__(self):
        return IT()  # 返回一个迭代器对象


obj = Foo()  # 创建一个可迭代对象

for item in obj:  # 循环可迭代对象时，内部先执行obj.__iter__并获取迭代器对象；不断执行迭代器对象的next方法。
    print(item)
