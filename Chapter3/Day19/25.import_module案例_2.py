# 传统导入模块方法：
from requests import exceptions

# 字符串导入方法
from importlib import import_module  # 先导入import_module,再使用

m = import_module("requests.exceptions")  # 注意：最小只能导入模块，无法进一步导入模块内的成员
