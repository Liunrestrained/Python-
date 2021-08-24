'''请创建一个列表，并在列表中初始化：0、1、2、3、4、5、6、7、8、9...299 整数元素。'''
# 方法1：
app = []
for i in range(300):
    app.append(i)

'''# 列表法：
list_1 = [i for i in range(10)]
list_2 = [[i, i] for i in range(10)]
list_3 = [[i, i] for i in range(10) if i > 5]

# 集合法：
set_1 = {i for i in range(10)}
set_2 = {{i, i} for i in range(10)}
set_3 = {{i, i} for i in range(10) if i > 5}

# 字典法：
dict_1 = {i: i for i in range(10)}
dict_2 = {{i: i} for i in range(10)}
dict_3 = {{i: i} for i in range(10) if i > 5}'''

# 元组法：
data = (l for l in range(10))  # 不会立即执行内部循环去生成数据，而是得到一个生成器。
print(data)
for i in data:
    print(i)
