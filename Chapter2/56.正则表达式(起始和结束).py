import re

'''要求用户必须以指定的内容开头和结尾'''
# ^  开头
# $  结尾
text = "STARSKY8816@gmail.com"
data = re.findall("^\w+@\w+.\w+$", text, re.ASCII)
print(data)

text_ = "啊STARSKY8816@gmail.com啊"
data_ = re.findall("^\w+@\w+.\w+$", text_, re.ASCII)
print(data_)
