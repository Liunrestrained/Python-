# 打印1、2、3、4、5、6、8、9、10
'''
for i in range(1, 11):
    if i == 7:
        pass
    else:
        print(i)
'''

# 当n为1或者2时，打印100以内的奇数。
'''
n = 1
while n < 100:
    if n % 2 == 1:  # 余数为1打印奇，余数为0打印偶。
        print(n)
    n += 1
'''

# 打印1-100的和
'''
n = 0
for i in range(1, 101):
    n += i
print(n)
'''

# 打印1-100内，奇数为正，偶数为负的所有整数的和。即1-2+3-4+5-6+7…-100=?
'''
n = 0
for i in range(1, 101):
    if i % 2 == 1:
        n += i
    else:
        n -= i
print(n)
'''

