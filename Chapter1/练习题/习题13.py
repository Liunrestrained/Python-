# 打印99×99口诀表
for i in range(1, 100):  # 乘数，每循环一次
    for l in range(1, i + 1):  # 被乘数从1开始，到乘数加1为结束
        print("{}×{}={}".format(l, i, l * i), end=" ")  # 两者相乘  去除当前循环的换行符
    print("")  # 给每一阶循环换换行一次