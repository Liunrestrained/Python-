# 使用open打开文件时，每次都需要手动close关闭文件，否则会需要退出程序才会自动关闭，浪费内存，或者引起其它错误
# 而使用with上下文管理，则可以自动关闭文件
with open(r"D:\draft\后来.txt", mode="rt", encoding="utf-8")as file:
    f = file.read()
    print(f)
