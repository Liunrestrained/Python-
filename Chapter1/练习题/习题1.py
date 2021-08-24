'''写代码实现对用户输入值的判断，是否为整数。如果是则转换为整型并输出，否则直接输出"请输入数字"。'''

while True:
    enter = input("请输入").strip()
    if enter.isdecimal() == True:
        print(int(enter))
        break
    else:
        print("请输入数字")
        continue