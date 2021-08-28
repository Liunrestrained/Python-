class Foo(object):

    def __setitem__(self, key, value):
        print(key, value)

    def __getitem__(self, item):
        print(item)

    def __delitem__(self, key):
        print(key)


obj = Foo()

# 集成类似字典的语法操作方法
obj["xxx"] = 123  # 自动触发类中__setitem__
obj["ooo"]  # 自动触发类中__getitem__
del obj["ooo"]  # 自动触发类中__delitem__
'''在Falsk源码中会用到'''
