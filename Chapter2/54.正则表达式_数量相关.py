import re

# *重复0次或更多次
n1 = "他是2爷，你是爷，我是22222爷爷爷"
n1_list = re.findall("是2*爷", n1)
print(n1_list)

# + 重复1次或者更多次
n2 = "他是2爷，你是爷，我是22222爷爷爷"
n2_list = re.findall("是2+爷", n2)
print(n2_list)

# ? 重复0次或者1次
n3 = "他是2爷，你是爷，我是22222爷爷爷"
n3_1 = re.findall("是2?爷", n3)
print(n3_1)

# {n} 重复n次,规定数据类型，以及后面重复的次数
n4 = "他是2爷，你是爷，我是22243534爷爷爷"
n4_1 = re.findall("2\d{4}", n4)
print(n4_1)

# {n,}重复n次或更多次
n5 = "楼主太牛逼了，在线想要 442662578@qq.com和xxxxx@live.com谢谢楼主，手机号也可15131255789，搞起来呀"
n5_1 = re.findall("\d{9,}", n5)
print(n5_1)

# {n,m}重复n~m次
n6 = "楼主太牛逼了，在线想要 442662578@qq.com和xxxxx@live.com谢谢楼主，手机号也可15131255789，搞起来呀"
n6_1 = re.findall("\d{9,11}", n6)
print(n6_1)
