'''
CPU个数
程序一般创建多个进程(利用CPU多核的优势)

'''

import multiprocessing

'''print(multiprocessing.cpu_count())  # 12'''

if __name__ == '__main__':
    count = multiprocessing.cpu_count()
    for i in range(count - 1):  # 还有个主进程，所以要-1
        p = multiprocessing.Process(target=xxxx)
        p.start()
