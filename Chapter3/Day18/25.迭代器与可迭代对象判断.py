from collections.abc import Iterator, Iterable

v1 = [11, 22, 33]
print(isinstance(v1, Iterator))  # False  判断是否是迭代器；判断依据是有__iter__和__next__，迭代器都有，可迭代对象只有__iter__
v2 = v1.__iter__()  # 执行iter方法，返回一个迭代器对象v2
print(isinstance(v2, Iterator))  # True

v3 = [11, 22, 33, 44]
print(isinstance(v3, Iterable))  # True  判断是否有__iter__且返回迭代器对象  不能单以Iterable判断是否为可迭代对象，因为迭代器也有__iter__
# 可以结合Iterator、Iterable一起来判断，即F\T，不是迭代器，但是能返回迭代器对象，那么就是可迭代对象！
v4 = v3.__iter__()
print(isinstance(v4, Iterable))  # True
