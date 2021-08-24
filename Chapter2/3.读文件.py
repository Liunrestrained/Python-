'''在读文件时，若没有源文件则会报错'''
file_object = open(r"D:\draft\莫斯科没有眼泪.txt", mode="rt", encoding="utf-8")

print(file_object.read())  # 读全部

print(file_object.read(3))  # 读3个字节

print(file_object.readline())  # 读1行

print(file_object.readlines())  # 都所有行，每一行作为列表的一个元素

for i in file_object:  # 循环读文件法，readlines加强版，适用于读大文件
    print(i.strip())
file_object.close()
