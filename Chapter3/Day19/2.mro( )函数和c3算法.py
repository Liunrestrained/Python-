'''当类中存在复杂的继承关系时，使用mro()函数，可以清晰地获取当前类的完整的继承关系，也就是成员的查找顺序。'''
'''总结继承关系的判断方法：从左到右，深度优先，大小钻石，留住顶端'''


class A(object):
    pass


class B(A):
    pass


class C(A):
    pass


class D(B):
    pass


class E(C):
    pass


class F(D, E):
    pass


print(F.mro())
'''
mro(F) = [F] + merge(mro(D), mro(E), [D, E])
mro(D) = [D, B]
mro(B) = [B, A]
mro(E) = [E, C]
mro(C) = [C, A]

mro(F) = [F] + merge([D, B], [E, C], [D, E])
mro(F) = [F,D,B,E,C]

mro(F) = [F,D,B,E,C,A,object]
'''
