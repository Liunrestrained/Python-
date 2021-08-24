import os  # 路径模块

data = os.path.exists(r"C:\Users\朱谢天\Desktop\老男孩全栈开发课程笔记.md")  # 判断路径是否存在
# print(data)  # 返回T或者R
if data:
    print("找到了文件")
    pass
else:
    print("路径不存在！")