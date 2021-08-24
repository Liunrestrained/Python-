import time
from datetime import datetime, timezone, timedelta

# 本地当前时间
v1 = datetime.now()
print(v1)

# 当前东7区时间
tz = timezone(timedelta(hours=7))
v2 = datetime.now(tz)
print(v2)

# 当前UTC时间
v3 = datetime.utcnow()
print(v3)

# 时间的加减
v4 = v1 + timedelta(days=140, minutes=5)  # 当前时区的时间再140天5分钟后的日期时间
print(v4)

# datetime之间相减，计算间隔时间（不能相加）
data = v1 - v3
print(data.days, data.seconds / 60 / 60, data.microseconds)

# 字符串格式的时间  ---> 转换为datetime格式时间
text = "2021-8-19"
v5 = datetime.strptime(text, '%Y-%m-%d')  # %Y 年，%m，月份，%d，天。
print(v5)

# datetime格式 ----> 转换为字符串格式
v6 = v1.strftime("%Y-%m-%d %H:%M:%S")
print(v6)

# 时间戳格式 --> 转换为datetime格式
ctime = time.time()
v7 = datetime.fromtimestamp(ctime)
print(v7)

# datetime格式 ---> 转换为时间戳格式
val = v1.timestamp()
print(val)
