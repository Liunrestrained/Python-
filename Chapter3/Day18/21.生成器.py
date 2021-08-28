# 创建生成器函数
def func():
    yield 1  # 函数中出现yield，那么他就是一个生成器函数
    yield 2


# 生成器函数后面加上括号就成了生成器对象
# 创建生成器对象（内部是根据生成器类generator创建的对象），生成器类的内部也声明了：__iter__、__next__方法，完全符合迭代器的定义规则，所以生成器也可以算是一种特殊的迭代器。
obj1 = func()

v1 = next(obj1)
print(v1)

v2 = next(obj1)
print(v2)

v3 = next(obj1)
print(v3)

obj2 = func()
for item in obj2:
    print(item)

# 如果按照迭代器的规定来看，其实生成器类也是一种特殊的迭代器类（生成器也是一种特殊的迭代器）
