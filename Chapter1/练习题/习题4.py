'''补充代码实现用户认证。
需求：提示用户输入手机号、验证码，全都验证通过之后才算登录成功（验证码大小写不敏感）'''

import random

while True:
    code = random.randrange(1000, 9999)  # 生成动态验证码
    msg = "欢迎登录PythonAV系统，您的验证码为：{},手机为号：{}".format(code, "15131266666")
    print(msg)
    enter = input("输入手机号、验证码,英文逗号区分")
    data = enter.split(",")
    if data[0] == "15131266666" and data[1] == str(code):
        print("登陆成功")
        break
    else:
        print("登陆失败")
        continue
