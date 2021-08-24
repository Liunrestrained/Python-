def func():
    print(11)

v1 = func()
print(v1)  # None

def coom():
    print(123)
    c = 123
    return c,  # return后面有有逗号，就会转换为元组来返回
    print(234)  # 遇到return后，函数就停止执行了
    print(456)

print(coom())