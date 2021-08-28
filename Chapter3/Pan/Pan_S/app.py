'''0.启动程序唯一入口'''
from Pan.Pan_S.src.server import Socket
from Pan.Pan_S.src.function import Function

if __name__ == '__main__':
    implement = Socket()  # 实例化对象
    implement.run(Function)  # 将方法类当作参数传递给run
