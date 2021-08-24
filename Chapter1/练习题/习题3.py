'''写代码实现一个整数加法计算器(两个数相加)。需求：提示用户输入：5+9或5+9或5+9，计算出两个值的和（提示：先分割再转换为整型，再相加）'''

enter = input("输入n+n格式的内容").strip()
data = enter.split("+")
sum = int(data[0]) + int(data[1])
print(sum)
