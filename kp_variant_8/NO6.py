def f(s):
    n = -5
    while s > 10:
        s = s - 8
        n = n + 3
    return n
a = [i for i in range(10000) if f(i) == 67]
print(max(a), min(a))