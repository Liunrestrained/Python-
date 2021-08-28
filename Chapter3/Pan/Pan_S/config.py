'''0.5配置文件：存放服务端IP、端口、父文件夹路径、用户云文件文件夹路径、用户注册表文件路径，使用时直接导入变量名'''
import os
import time

IP = "127.0.0.1"
Port = 8001

file_path = os.path.dirname(os.path.abspath(__file__))
file_personal = os.path.join(file_path, "files")
file_xlsx = os.path.join(file_path, "db", "User registration information form.xlsx")

print("啊~呼~！你终于想起唤醒我了！臭宝！(*/ω＼*)")
time.sleep(2)
print("(●'◡'●)我在等一个有缘人...")