# geatter , 去对象中获取成员
v1 = getattr(对象, "成员名称")
v2 = getattr(对象, "成员名称", 不存在时的默认值)  # 一般设置为None

# setattr , 去对象中设置成员
setattr(对象, "成员名称", 值)

# hasattr , 对象中是否包含成员
v1 = hasattr(对象, "成员名称")  # True/False

# delattr , 删除对象中的成员
delattr(对象, "成员名称")
