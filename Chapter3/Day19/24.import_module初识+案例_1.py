'''在Python中导入一个模块，除了import方法之外，还可以用字符串的形式导入。'''
# 示例1
# import random
#
# v1 = random.randint(1, 100)

# 字符串形式导入
from importlib import import_module  # 先导入import_module,再使用

m = import_module("random")

v1 = m.randint(1, 100)

print(v1)