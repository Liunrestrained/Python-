class Foo(object):
    def __init__(self, name, age, year):
        self.name = name
        self.age = age
        self.year = year


obj = Foo("李健", 12, 2021)
print(obj.__dict__)  # {'name': '李健', 'age': 12, 'year': 2021}
'''自动去获取这个类的所有实例变量，以字典的形式展示出来'''
'''写前后端分离项目时会用到'''
