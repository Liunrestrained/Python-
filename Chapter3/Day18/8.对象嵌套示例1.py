class Student(object):
    """ 学生类 """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def message(self):
        data = "我是一名学生，我叫:{},我今年{}岁".format(self.name, self.age)
        print(data)


s1 = Student("武沛齐", 19)
s2 = Student("Alex", 19)
s3 = Student("日天", 19)


class Classes(object):
    """ 班级类 """

    def __init__(self, title):
        self.title = title
        self.student_list = []

    def add_student(self, stu_object):
        self.student_list.append(stu_object)

    def add_students(self, stu_object_list):
        for stu in stu_object_list:
            self.add_student(stu)

    def show_members(self):
        for item in self.student_list:
            # print(item)
            item.message()


c1 = Classes("三年二班")
c1.add_student(s1)
c1.add_students([s2, s3])

print(c1.title)
print(c1.student_list)
