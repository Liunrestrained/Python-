'''简单的条件语句，可以基于三元运算来实现；同时，lambda表达式可以和三元运算结合使用'''

# 结果 = 条件成立时  if  条件  else  不成立

data = lambda a: print("大了") if a > 6 else print("小了")
data(999)
