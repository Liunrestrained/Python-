'''maxsplit： 最多可划分的数量，指定此参数，将会把原字符串拆分成maxsplit + 1 部分如果不指定该参数或是-1的话，将不会受到限制。'''

s1 = "a.b.c.d.e.f"  # 设置字符拆时，我默认用空格分割开

a1 = s1.split(".", maxsplit=1)  # 此处指定按照空格分开，分割成maxsplit+1份
print(a1)  # ['a', 'b c d e f']

a2 = s1.split(".", maxsplit=2)  # 此处不指定分割符号，自己推导出用空格分割成maxsplit+1份
print(a2)  # ['a', 'b', 'c d e f']

a3 = s1.split(".", maxsplit=10)  # 当我设置的分割份数超过了既有字符串的可分割个数，默认按照最大可分割数分割
print(a3)  # ['a', 'b', 'c', 'd', 'e', 'f']
