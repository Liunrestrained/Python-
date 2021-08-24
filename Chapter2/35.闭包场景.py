'''闭包：就是将数据封装在一个区域中，等到使用时再去里面取'''

def task(arg):
    def inner():
        print(arg)

    return inner


v1 = task(11)
v2 = task(22)
v3 = task(33)
v1()
v2()
v3()
