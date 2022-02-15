a1 = a = (81 ** 18 - (81 ** 8 - 1) * ((8 + 1) ** 8 + 1) // 8 - 8)
print(a)
s = ''
while a:
    s = str(a % 3) + s
    a //= 3
print(s)
print(s.count('1'))