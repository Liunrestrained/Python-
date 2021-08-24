import re

# 指定字符串，在文本中找出同样的字符串——可用于计算某个字符串在文中的出现次数
v0 = "众里寻他千百度，蓦然回首，那人却在灯火阑珊处。"
v0_list = re.findall("灯火", v0)
print(v0_list)

# [abc]匹配文中的a或b或c字符——可用于计算某个字符串在文中的出现次数
v1 = "qapp,qapple,out,anothqer"
v1_list = re.findall("[abc]", v1)
print(v1_list)

v1_list_v1 = re.findall("q[abc]", v1)
print(v1_list_v1)

# [^abc]匹配除了abc以外的其它字符
v2 = "asfwegasdrwegdfbsf"
v2_list = re.findall("[^abc]", v2)
print(v2_list)

# [a-z]匹配a~z的任意字符(0~9也可以)
v3 = "aqaqasfasca23rfwqaefqavqa5 wasdiab hdbas啊手机打开吧啊"
v3_list = re.findall("[a-z]", v3)
print(v3_list)
v3_list_v3 = re.findall("q[a-z]", v3)
print(v3_list_v3)

# . 代指除了换行符以外的任意字符,一个点代表一个字符
v4 = "aodabdacdabbdabbbda33da奇怪奇怪d"
v4_list = re.findall("a.d", v4)
print(v4_list)

v4_list_v1 = re.findall("a.+d", v4)  # 贪婪匹配
print(v4_list_v1)

v4_list_v2 = re.findall("a.+?d", v4)  # 贪婪匹配
print(v4_list_v2)

# \w 代指 字母 或数字 或下划线（汉字）。
v5 = "习大大_毛泽东，胡锦涛"
v5_list = re.findall("习\w+，", v5)
print(v5_list)

# \d 代指数字
v6 = "鄂3586，湘8899"
v6_list = re.findall("鄂\d", v6)
print(v6_list)

v6_list_v1 = re.findall("鄂\d+", v6)
print(v6_list_v1)

# \s 代指任意的空白符，包括空格，制表符等
v7 = "朱3586 刘1234 朱朱7789 朱6朱朱 朱 李3422"
v7_list = re.findall("朱\w+\s", v7)
print(v7_list)
