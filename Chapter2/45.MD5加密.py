import hashlib  # 字符串加密模块


def encrypt(origin):
    origin_bytes = origin.encode("utf-8")  # 将十进制密码转换为bytes类型
    md5_object = hashlib.md5()  # 创建md5的加密方式
    md5_object.update(origin_bytes)  # 将bytes类型的密码，通过创建的md5加密方法进行加密
    return md5_object.hexdigest()  # 返回加密后的密文


p1 = (encrypt("zxt@225011"))
print(p1)
