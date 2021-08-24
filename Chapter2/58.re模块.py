import re

# findall 获取匹配到的所有数据
text = "dsf130429191912015219k13042919591219521Xkk"
data_list = re.findall("(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X)", text)
print(data_list)

# match ,从起始位置开始，匹配成功则返回一个对象，未匹配成功则返回None。
text_1 = "大小逗2B最逗3B欢乐"
data_1 = re.match("逗\db", text_1)
print(data_1)

text_2 = "逗2B最逗3B欢乐"
data_2 = re.match("逗\dB", text_2)
if data_2:
    content = data_2.group()  # "逗2B"  group()用于截获分段
    print(content)

# search 浏览整个字符串去匹配第一个

a1 = "逗2B最逗3B欢乐"
a2 = re.search("逗\dB", a1)
print(a2.group())

# sub 替换所有匹配成功的位置

b1 = "逗2B最逗3B欢乐"
b2 = re.sub("\dB", "沙雕", b1)
print(b2)

c1 = "逗2B最逗3B欢乐"
c2 = re.sub("\dB", "沙雕", b1, 1)
print(c2)

# split 根据匹配成功的位置进行分割

d1 = "逗2B最逗3B欢乐"
d2 = re.split("\dB", b1)
print(d2)

e1 = "逗2B最逗3B欢乐"
e2 = re.split("\dB", e1, 1)
print(e2)

# finditer  # 获取匹配成功的位置
f1 = "逗2B最逗3B欢乐"
f2 = re.findall("\dB", f1)
print(f2)

g1 = "逗2B最逗3B欢乐"
g2 = re.finditer("(?P<xx>\dB)", g1)
for i in g2:
    print(i.groupdict())  # 将获取到的对应信息，以规定的key转换为字典
    # {'xx': '2B'}
    # {'xx': '3B'}

h1 = "dsf130429191912015219k13042919591219521Xkk"
h2 = re.finditer("\d{6}(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})\d{3}[\d|X]", h1)
for item in h2:
    info_dict = item.groupdict()
    print(info_dict)
