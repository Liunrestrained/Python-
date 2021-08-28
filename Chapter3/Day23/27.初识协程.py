# 协程是程序员通过代码实现的一个一种操作。
# 协程可以被称为微线程，是一种用户态内的上下文切换技术。即：通过一个线程实现代码块之间相互切换执行(来回跳着执行).

# 在Python中有很多方式可以实现协程，例如：

# greenlet, 需要三方模块。pip install greenlet
'''from greenlet import greenlet

def func1():
    print(1)
    gr2.switch()  # 切换到执行函数2
    print(2)
    gr2.switch()  # 切换到执行函数2
def func2():
    print(3)
    gr1.switch()  # 切换到执行函数1
    print(4)
gr1 = greenlet(func1)  # 执行函数1
gr2 = greenlet(func2)  # 执行函数2'''


# yield
'''def func1():
    yield 1
    yield from func2()
    yield 2
def func2():
    yield 3
    yield 4
f1 = func1()
for i in f1:
    print(i)
'''


'''
虽然上述两种都实现了协程，但这种编写代码的方式没啥意义。
这种来回切换执行，可能反倒让程序的执行速度更慢了（相比较于串行）。
'''