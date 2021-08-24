import os

if not os.path.exists(r"D:\draft"):
    os.makedirs(r"D:\draft")
else:
    print("路径已存在")