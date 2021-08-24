import re

# 提取数据区域  最终只会打印括号内的规定的内容
data = "楼主太牛逼15131355555了15131255555，在线想要 442662578@qq.com和xxxxx@live.com谢谢楼主，手机号也可15131255789，搞起来呀"
data_list = re.findall("15131(2\d{5})", data)
print(data_list)  # ['255555', '255789']

data_1 = "楼主太牛逼了，在线想要 442662578@qq.com和xxxxx@live.com谢谢楼主，手机号也可15131255789，搞起来15131266666呀"
data_1_list = re.findall("15(13)1(2\d{5})", data_1)
print(data_1_list)

text = "楼主太牛逼了，在线想要 442662578@qq.com和xxxxx@live.com谢谢楼主，手机号也可15131255789，搞起来呀"
data_list_2 = re.findall("(15131(2\d{5}))", text)
print(data_list_2)  # [('15131255789', '255789')]

# 获取指定区域 + 或条件
a1 = "楼主15131root太牛15131alex逼了，在线想要 442662578@qq.com和xxxxx@live.com谢谢楼主，手机号也可15131255789，搞起来呀"
a2 = re.findall("15131(2\d{5}|r\w+太)", a1)
print(a2)

a3 = "楼主15131root太牛15131alex逼了，在线想要 442662578@qq.com和xxxxx@live.com谢谢楼主，手机号也可15131255789，搞起来呀"
a4 = re.findall("(15131(2\d{5}|r\w+太))", a3)
print(a4)