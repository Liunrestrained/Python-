file_object = open(r"D:\draft\莫斯科没有眼泪.txt", mode="wb")
file_object.write("寒冷的季节，在莫斯科的深夜".encode("utf-8"))
file_object.close()

file = open(r"D:\draft\莫斯科没有眼泪.txt", mode="rt", encoding="utf-8")
print(file.read())
file.close()