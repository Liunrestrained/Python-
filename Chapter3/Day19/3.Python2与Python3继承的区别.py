# 2.2以及之前版本，经典类：未继承object【从左到右、深度优先、大小钻石、不留顶端】
class Foo:
    pass


# 2.3版本开始，新式类：直接获取、间接继承object【从左到右、深度优先、大小钻石、留住顶端--C3算法】
class BBA(object):
    pass


# 直接获取与间接继承object：
class Base(object):
    pass


class BAT(Base):
    pass


# Py3开始
# 新式类，直接丢弃经典类，只保留新式类：【从左到右，深度优先，大小钻石，留住顶端 -- C3算法】
class Fo:
    pass


class Bar(object):
    pass
