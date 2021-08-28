num1 = input("输入数字")
num2 = input("输入数字")
try:
    num1 = int(num1)
    num2 = int(num2)
    num = num1 + num2
    print(num)
except Exception as e:
    print("输入错误")
