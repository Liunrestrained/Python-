import os

a = os.path.abspath(__file__)  # 当前程序的路径   D:\Pycharm Project\Chapter2\22.程序当前路径.py
b = os.path.dirname(a)  # 当前程序的上级文件夹路径  D:\Pycharm Project\Chapter2

c = os.path.join(b, "xxx", "xxx.txt")  # 路径拼接  D:\Pycharm Project\Chapter2\xxx\xxx.txt