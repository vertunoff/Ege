a = [int(i.strip()) for i in open('1017.txt').readlines()]
aa = []
for i in range(len(a) - 1):
    x = a[i] + a[i + 1]
    if len(str(x)) == 3 and x % 10 > (x // 10) % 10:
        aa.append(x)
print(len(aa), min(aa))