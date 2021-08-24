print(abs(-1))  # 绝对值
print(pow(2, 3))  # 指数
print(sum([1, 2, 30, -1]))  # 求和
print(divmod(9, 2))  # 求商和余数
print(round(3.14159, 2))  # 小数点后保留n位置

print(min(1, 2, 4))  # 最小值
print(max(1, 2, 3))  # 最大值
print(max([1, 2, 3, 4]))  # 列表内最大值
print(max([1, 2, 3, 55, -999], key=lambda x: x * 10))  # 列表内每一个元素*10值最大的元素
print(all([1, 0, 2]))  # 是否全部为True
print(any([1, 2, 4, 0, -1]))  # 是否存在True

print(bin(10))  # 十进制转换为二进制
print(oct(10))  # 十进制转换为八进制
print(hex(10))  # 十进制转换为十六进制

v1 = ord("天")  # 获取字符对应的unicode码点（十进制）
print(v1, hex(v1))
v2 = chr(22825)  # 根据unicode十进制码点获取对应的字符
print(v2)

str()  # unicode编码，可哈希
int()  # 整型，可哈希
float()  # 浮点型
bytes()  # utf、gbk编码
print("大力".encode("utf-8"))  # bytes类型
print(bytes("张伟", encoding="utf-8"))  # bytes类型
bool()  # 布尔值，判断，可哈希
list()  # 列表[]，有序可变可重复，不可哈希
set()  # 集合{}，无序可变不重复，不可哈希
tuple()  # 元组()，有序不可变，可哈希
dict()  # 字典，无序可变键不重复，键可哈希

len()  # 长度
print()  # 打印
input()  # 获取
open()  # 打开
type()  # 获取数据类型
range()  # 循环几次
enumerate()  # 循环的次数对应序号
id()  # 数据的id
hash()  # 哈希值
help()  # 帮助，终端使用
zip()  # 解压类型
callable()  # 是否可以执行
sorted()  # 排序



