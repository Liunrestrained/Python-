# 导入模块exceptions，获取exceptions中的InvalidURL类。
from requests.exceptions import InvalidURL



# 错误方式
from importlib import import_module

m = import_module("requests.exceptions.InvalidURL")  # 报错，import_module只能导入到模块级别。



# 导入模块
from importlib import import_module

m = import_module("requests.exceptions")
# 去模块中获取类
cls = m.InvalidURL
