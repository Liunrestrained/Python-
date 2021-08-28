# 反射提供了一种更加灵活的方式，可以实现以字符串的形式去对象中操作成员。

class Person(object):

    def __init__(self, name, tel):
        self.name = name
        self.tel = tel

    def show(self):
        card = "姓名{},电话{}".format(self.name, self.tel)
        print(card)


# user_object = Person("胡歌", 18986669888)
#
# # 以 对象.成员 的格式去获取数据
# n1 = user_object.name
# print(n1)
# n2 = user_object.tel
# print(n2)
# user_object.show()

# # 对象.成员 的格式去创建或更改数据
# user_object.name = "彭于晏"


user = Person("张大仙", 16688886666)
# getattr 获取成员
v1 = getattr(user, "name")
print(v1)
v2 = getattr(user, "tel")
print(v2)

v3 = getattr(user, "show")
v3()
# 或者 getattr(user, "show")()

# setattr 设置\更改成员
setattr(user, "name", "大张伟")
