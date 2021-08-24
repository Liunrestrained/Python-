import re

enter = input("请输入邮箱")
email = re.findall("^\w+@\w+.\w+$", enter, re.ASCII)
if not email:
    print("邮箱格式错误")
else:
    print("输入正确")
