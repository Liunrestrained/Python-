'''def func():
    print(123)


data_list = [func for i in range(10)]

print(data_list)
print(func)'''

'''def func(num):
    return num + 100


data_list = [func(i) for i in range(10)]

print(data_list)'''

'''def func(x):
    return x + i


data_list = [func for i in range(10)]

val = data_list[0](100)
print(val)'''

'''# 新浪微博面试题
data_list = [lambda x: x + i for i in range(10)]  # [函数,函数,函数]   i=9
# 循环的时候，函数体x+1不会执行，没有任何变化，就当作不知道函数体，所以得出来的都是函数；执行完毕后i=9。
v1 = data_list[0](100)
v2 = data_list[3](100)
print(v1, v2)  # 109 109'''


