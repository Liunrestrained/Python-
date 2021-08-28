class Student(object):
    """ 学生类 """

    def __init__(self, name, age, class_object):
        self.name = name
        self.age = age
        self.class_object = class_object

    def message(self):
        data = "我是一名{}班的学生，我叫:{},我今年{}岁".format(self.class_object.title, self.name, self.age)
        print(data)


class Classes(object):
    """ 班级类 """

    def __init__(self, title):
        self.title = title


c1 = Classes("Python全栈")
c2 = Classes("Linux云计算")

user_object_list = [
    Student("武沛齐", 19, c1),
    Student("Alex", 19, c1),
    Student("日天", 19, c2)
]

for obj in user_object_list:
    print(obj.name, obj.age, obj.class_object.title)
