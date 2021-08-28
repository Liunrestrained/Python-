v1 = [1, 2, 3, 4]
print(dir(v1))
# v1是一个可迭代对象，因为在列表中声明了一个__iter__方法，并返回了一个迭代器对象
v2 = v1.__iter__()  # 执行iter方法，得到一个迭代器对象v2，可以被迭代(for循环)
# v3 = v2.__next__()
for i in v2:
    print(i)
# 常见的数据类型set tuple dict list都是可迭代对象
