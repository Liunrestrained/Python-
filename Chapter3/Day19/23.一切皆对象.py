'''对象是对象、类是对象、模块也是对象
由于反射支持以字符串的形式去对象中操作成员【等价于 对象.成员 】，所以，基于反射也可以对类、模块中的成员进行操作。
简单粗暴：只要看到 xx.oo 都可以用反射实现。'''


# 示例1：
class Person(object):
    title = "武沛齐"


v1 = Person.title
print(v1)
v2 = getattr(Person, "title")
print(v2)

# 示例2
import re

v1 = re.match("\w+", "dfjksdufjksd")
print(v1)

func = getattr(re, "match")
v2 = func("\w+", "dfjksdufjksd")
print(v2)
