'''8.补充代码实现数据拼接'''

data_list = []
while True:
    hobby = input("请输入你的爱好（Q/q退出）：")
    if hobby.upper() == 'Q':
        break
    # 把输入的值添加到 data_list 中，如：data_list = ["小姨子","哥们的女朋友"]
    data_list.append(hobby)
    # 将所有的爱好通过符号 "、"拼接起来并输出
print("、".join(data_list))
