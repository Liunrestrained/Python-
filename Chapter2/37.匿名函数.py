'''匿名函数：基于lambda表达式实现定义一个可以没有名字的函数'''
'''函数格式为：lambda 参数: 函数体'''
'''参数支持任意参数；函数体只支持单行代码；默认将函数体单行代码执行的结果返回给函数的执行者'''

# data = lambda x, y: x + y + 10
# res = data(1, 2)
# print(res)

func = lambda a: a.replace("死亡", "**")
b = func("死亡如风")
print(b)
