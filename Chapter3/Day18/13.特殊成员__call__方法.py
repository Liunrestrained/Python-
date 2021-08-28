class Foo(object):
    def __call__(self, *args, **kwargs):
        print("执行call方法")


obj = Foo()
obj()  # 在对象后面加“括号”，就会默认执行call方法！

'''常见不多，一般在falsk、DJiango等源码的入口部分会见到'''
