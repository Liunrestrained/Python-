# 当你清楚知道执行次数时，用它！
for i in range(10):
    print(688)


# 当你并不清楚要循环多少次时，使用它！
number = 0
while True:
    number += 1
    if number == 10:
        print("运行结束")
        break

# break 结束循环
# continue 从这里折返至循环开始，重新循环
# pass  啥都不做
