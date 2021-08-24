# import sys
# print(sys.path)

'''想要导入任意的模块和包，都必须写在如下的路径，才能够被找到。
也可以自己手动在sys.path中添加指定路径，然后再导入'''
import sys

sys.path.append("路径A")

import xxxx  # 导入路径A下的一个xxxx.py文件
