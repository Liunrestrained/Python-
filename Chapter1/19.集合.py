'''集合是可变、无序、不重复的容器'''
v = {"刘亦菲", "王祖贤", "周润发"}
u = {"古天乐", "刘德华", "王祖贤"}
v.add("张国荣")  # 添加元素
v.discard("刘亦菲")  # 删除元素
print(v.intersection(u))  # 取得两个集合的交集  或者 print(v & u)
print(v.union(u))  # 或者 print(v|u)
print(v.difference(u))  # 取得差集，v有U没有；替换位置则是u有v没有的差集  或者print(v-u)  print(u-v)
print(v)