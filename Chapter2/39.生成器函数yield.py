'''当函数中有yield存在时，这个函数就是生成器函数'''

'''def func():
    print(11)
    yield 1
    print(22)
    yield 2
    return   # 结束或者中途遇到return，就会报错StopIteration
    print(33)


n = func()  # 执行生成器函数
n1 = next(n)  # 执行第一层函数，并将yield后面的值赋值给n1
print(n1)  # 打印yield返回的值
n2 = next(n)  # 同上
print(n2)
n3 = next(n)  # 停止重复'''


def func():
    print(111)
    yield 1

    print(222)
    yield 2

    print(333)
    yield 3

    print(444)


data = func()
for i in data:
    print(i)
