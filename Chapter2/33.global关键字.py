'''通常情况下，局部变量可以修改全局变量，但是无法给全局变量进行重新赋值，除非用global函数'''
NUMBER = 99
LIST = ["大海", "大河"]


def func():
    global NUMBER
    NUMBER = 77
    print(NUMBER)
    LIST = ["大鱼", "大肉"]
    print(LIST)


func()

print(NUMBER)
print(LIST)
