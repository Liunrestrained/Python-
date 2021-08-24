import json

# Python中的数据类型格式
data = [{"id": 1, "name": "诸葛大力", "age": 18}, {"id": 2, "name": "张伟", "age": 28}]

# 序列化
res = json.dumps(data)
print(res)

ress = json.dumps(data, ensure_ascii=False)
print(ress)

# JSON格式
data_string = '[{"id": 1, "name": "诸葛大力", "age": 18},{"id": 2, "name": "张伟", "age": 28}]'
# 反序列化
data_list = json.loads(data_string)
print(data_list)
