'''print函数默认会在末尾添加换行符'''
print("hello")
print("world")

'''不加换行符，什么符号都不加'''
print("hello", end="")  # 不加换行符
print("world")  # 加了换行符

'''加个空格'''
print("hello", end=" ")  # 加了空格
print("world", end=" ")