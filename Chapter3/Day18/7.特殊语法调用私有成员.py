class Foo:

    def __init__(self):
        self.__num = 123
        self.age = 22

    def __msg(self):
        print(123)


obj = Foo()
print(obj.age)
print(obj._Foo__num)  # 通过特殊的语法从外部调用私有成员，不建议使用，好好遵守语法规则。
obj._Foo__msg()
