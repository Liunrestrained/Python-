def foo():
    yield 2
    yield 2
    yield 2


def func():
    yield 1
    yield 1
    yield 1
    # foo()
    yield from foo()  # 可以跳转去执行foo()函数，而不是返回一个生成器对象，返回2 2 2
    yield 1
    yield 1


for item in func():
    print(item)
