class Police:
    """警察"""

    def __init__(self, name, role):
        self.name = name
        self.role = role
        if role == "队员":
            self.hit_points = 200
        else:
            self.hit_points = 500

    def show_status(self):
        """ 查看警察状态 """
        message = "警察{}的生命值为:{}".format(self.name, self.hit_points)
        print(message)

    def bomb(self, terrorist_list):
        """ 投炸弹，炸掉恐怖分子 """
        for terrorist in terrorist_list:
            terrorist.blood -= 200
            terrorist.show_status()


"""
p1 = Police("武沛齐","队员")
p1.show_status()
p1.bomb(["alex","李杰"])

p2 = Police("日天","队长")
p2.show_status()
p2.bomb(["alex","李杰"])
"""


class Terrorist:
    """ 恐怖分子 """

    def __init__(self, name, blood=300):
        self.name = name
        self.blood = blood

    def shoot(self, police_object):
        """ 开枪射击某个警察 """
        police_object.hit_points -= 5
        police_object.show_status()

        self.blood -= 2

    def strafe(self, police_object_list):
        """ 扫射某些警察 """
        for police_object in police_object_list:
            police_object.hit_points -= 8
            police_object.show_status()

    def show_status(self):
        """ 查看恐怖分子状态 """
        message = "恐怖分子{}的血量值为:{}".format(self.name, self.blood)
        print(message)


"""
t1 = Terrorist('alex')
t2 = Terrorist('李杰',200)
"""


def run():
    # 1.创建3个警察
    p1 = Police("武沛齐", "队员")
    p2 = Police("苑昊", "队员")
    p3 = Police("于超", "队长")

    # 2.创建2个匪徒
    t1 = Terrorist("alex")
    t2 = Terrorist("eric")

    # alex匪徒射击于超警察
    t1.shoot(p3)

    # alex扫射
    t1.strafe([p1, p2, p3])

    # eric射击苑昊
    t2.shoot(p2)

    # 武沛齐炸了那群匪徒王八蛋
    p1.bomb([t1, t2])

    # 武沛齐又炸了一次alex
    p1.bomb([t1])


if __name__ == '__main__':
    run()
