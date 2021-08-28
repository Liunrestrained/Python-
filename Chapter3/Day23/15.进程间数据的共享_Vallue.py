from multiprocessing import Process, Value, Array


def func(n, m1, m2):
    n.value = 888
    m1.value = 'a'.encode('utf-8')
    m2.value = "武"


if __name__ == '__main__':
    num = Value('i', 666)  # i = int，666就是默认初始化的值
    v1 = Value('c')  # 在c语言里面可以理解为a,b,c...这种单个的字符
    v2 = Value('u')  # 一个字符，包含多字节的中文字符

    p = Process(target=func, args=(num, v1, v2))  # 传给子进程，子进程可以修改，从而实现进程之间的“共享”
    p.start()
    p.join()

    print(num.value)
    print(v1.value)
    print(v2.value)


'''
此方法包含C语言的内容：
    'c': ctypes.c_char,  'u': ctypes.c_wchar,
    'b': ctypes.c_byte,(0-255，每8位1个字节，代表这几个区间的数，不带u可以为负数)  'B': ctypes.c_ubyte,(代指0-255) 
    'h': ctypes.c_short, 'H': ctypes.c_ushort,(代指0-65535) 
    'i': ctypes.c_int,   'I': ctypes.c_uint,  （其u表示无符号）(也就是0-多少)
    'l': ctypes.c_long,  'L': ctypes.c_ulong, 
    'f': ctypes.c_float(在底层使用32位存储的), 'd': ctypes.c_double(在底层用64位存储的，更精确)
'''