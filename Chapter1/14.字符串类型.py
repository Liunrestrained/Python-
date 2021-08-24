'''操作字符串的功能有哪些'''
# 1.判断字符串是否以***作为开头
website = "www.baidu.com"
print(website.startswith("www"))

# 2.判断字符串是否以***作为结尾
website = "www.baidu.com"
print(website.endswith("com"))

# 3.判断字符串是否为十进制数
n1 = "999"
print(n1.isdecimal())

# 4.除去字符串两边的空格、换行、制表符或者指定内容
n2 = " 我爱你，没有空格换行符号 "
print(n2.strip())
print(n2.rstrip())
print(n2.lstrip())
print(n2.strip("号 "))

# 5.字符串变大、小写
a1 = "bbc"
a2 = "BBC"
print(a1.upper())
print(a2.lower())

# 6.字符串内容替换
b1 = "唧唧复唧唧，木兰当户织"
print(b1.replace("唧唧", "吉吉"))

# 7.字符串切割
c1 = "http:\\www.baidu.com"
print(c1.split("."))
print(c1.split(".", 1))

# 8.字符串拼接
data_list = ["我爱你", "爱着你", "就像老鼠爱大米"]
print(",".join(data_list))
print("".join(data_list))

# 9.字符串转换为字节类型
lin = "弟妹"  # unicode
v1 = lin.encode("utf-8")
v2 = lin.encode("gbk")
print(v1)
print(v2)
v3 = v1.decode("utf-8")
v4 = v2.decode("gbk")
print(v3)
print(v4)

# 将字符串内容居中、靠左、靠右显示
b1 = "王大锤"
print(b1.center(10, "-"))
print(b1.ljust(10, "-"))
print(b1.rjust(10, "-"))

# 填充0
j1 = "1001"
print(j1.zfill(8))
