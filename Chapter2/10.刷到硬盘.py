f = open(r"D:\draft\莫斯科没有眼泪.txt", mode="a", encoding="utf-8")
f.write("可可爱爱，没的脑袋")
f.flush()  #  # 通常情况下，内容都被写入了缓冲区，然后才写入到硬盘；使用flush()直接刷入硬盘。
f.close()