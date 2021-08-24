name = 'root'


def outer():
    name = "武沛齐"

    def inner():
        nonlocal name  # 将上级定义域的变量修改
        name = 123

    inner()
    print(name)


outer()
print(name)
