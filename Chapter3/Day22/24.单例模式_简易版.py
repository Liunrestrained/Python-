class Singleton:
    instance = None

    def __init__(self, name):  # 再执行init
        self.name = name

    def __new__(cls, *args, **kwargs):
        # 返回空对象
        if cls.instance:  # instance不为空在，则执行
            return cls.instance  # 直接将这个对象返回
        cls.instance = object.__new__(cls)  # 为空，则创建一个空对象，赋值给类变量
        return cls.instance  # 将这个对象返回


'''要求实例化对象公用一个地址，就需要用到单例模式'''
obj1 = Singleton("add")
print(obj1)

obj2 = Singleton("pdd")
print(obj2)
