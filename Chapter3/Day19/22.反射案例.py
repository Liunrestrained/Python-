class Account(object):

    def login(self):
        pass

    def register(self):
        pass

    def index(self):
        pass


def run(self):
    name = input("请输入要执行的方法名称：")  # index register login xx run ..

    account_object = Account()
    method = getattr(account_object, name, None)  # index = getattr(account_object,"index")

    if not method:
        print("输入错误")
        return
    method()
