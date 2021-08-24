data_list = ["你爱我", "我爱你"]

data_list.append("蜜雪冰城甜蜜蜜")  # 尾部追加元素
data_list.insert(1, "两只老虎爱跳舞")  # 根据索引添加元素
data_list.remove("你爱我")  # 根据值删除，没找到会报错
data_list.pop(1)  # 根据索引删除某个元素
data_list.clear()  # 清空原列表

print(data_list)