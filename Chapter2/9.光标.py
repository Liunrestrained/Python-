with open(r"D:\draft\莫斯科没有眼泪.txt", mode="r", encoding="utf-8")as f:
    f.seek(6)  # 移动光标两个字符，6个字节
    print(f.read())
    p = f.tell()  # 获取光标当前的位置
    print(p)
# 在操作光标的时候，要注意字节规则，否则会报错！
