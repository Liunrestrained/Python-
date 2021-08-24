import os

a = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

b = os.path.join(a, "draft", "dd")
if os.path.exists(b):
    print("文件存在")
    f = open(r"{}\逍遥.txt".format(b), mode="r+", encoding="utf-8")
    g = f.read()
    f.write("岁月")
    print(g)
    f.close()
else:
    print("文件夹不存在,正在为您创建它")
    os.makedirs((b))
