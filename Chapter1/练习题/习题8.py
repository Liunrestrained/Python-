'''现有 `v1=123` 和 `v2=456`，请将这两个值转换为二进制，并将其二进制中的前缀 0b 去掉，
再补足为2个字节（16位），然后将两个二进制拼接起来，最终再转换为整型（十进制）。'''

a1 = bin(123)  # 0b1111011
a2 = bin(456)  # 0b111001000
b1 = a1.lstrip("0b")  # 1111011
b2 = a2.lstrip("0b")  # 111001000
c1 = b1.zfill(16)  # 0000000001111011
c2 = b2.zfill(16)  # 0000000111001000
d1 = c1 + c2
print(int(d1, base=2))
