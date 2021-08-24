'''假设要让你生成 300w个随机的4位数，并打印出来。'''

'''import random  # 随机模块

val = random.randint(1000, 9999)  # 设定随机数范围
print(val)'''

'''import random

data_list = []  # 创建完成后，list中储存了三百万个随机四位数，需要时，直接在里面获取即可
for i in range(3000000):
    val = random.randint(1000, 9999)
    data_list.append(val)
'''

import random  # 导入模块


def func(max):  # 创建函数
    for i in range(3000000):
        yield random.randint(1000, 9999)


data = func(3000000)
print(next(data))  # 执行一次取一次
# for j in data:  # 循环取得三百万次4位随机数
#     print(j)
