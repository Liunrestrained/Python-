'''父类、子类
基类、派生类'''


class Angel:

    def one(self):
        print("Angel.one")


class Bease(Angel):

    def two(self):
        print("Bease.two")


obj = Bease()
obj.two()
obj.one()

dea = Angel()
dea.one()
