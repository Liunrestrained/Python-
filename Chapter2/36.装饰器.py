import functools


def auth(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        '''执行函数之前'''
        print("我来组成头部")
        res = func(*args, **kwargs)
        '''执行函数之后'''
        print("我来组成胯子")
        return res

    return inner


@auth
def line():
    print("我来组成胸部")


line()
print(line.__name__)  # 不加functool函数，返回函数名字为inner;加了则返回line。
