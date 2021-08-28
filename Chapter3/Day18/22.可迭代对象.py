# 如果一个类中有__iter__方法且返回一个迭代器对象 ；则我们称以这个类创建的对象为可迭代对象。

class Foo(object):

    def __iter__(self):
        return  # 迭代器对象(生成器对象)


obj = Foo()  # obj是 可迭代对象。

# 可迭代对象是可以使用for来进行循环，在循环的内部其实是先执行 __iter__ 方法，获取其迭代器对象，然后再在内部执行这个迭代器对象的next功能，逐步取值。
for item in obj:
    pass
