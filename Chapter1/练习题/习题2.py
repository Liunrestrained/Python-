'''对用户输入的数据使用"+"切割，判断输入的值是否都是数字？提示：用户输入的格式必须是以下+连接的格式，如 5+9 、alex+999'''

while True:
    enter = input("请输入** + **格式的内容").strip()
    data = enter.split("+")
    if data[0].isdecimal() == True and data[1].isdecimal() == True:
        print("输入正确")
        break
    else:
        print("输入错误")
        continue