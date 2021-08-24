import time

# 获取当前时间戳（自1970-1-1 00:00）
v1 = time.time()
print(v1)  # 1629357553.561562秒≈51年

# 时区
v2 = time.timezone

# 停止n秒，再执行后续的代码。
time.sleep(5)
