def f(n):
    n = bin(n)[2:]
    n = '0' * (8 - len(n)) + n
    n = n.replace('0', 'a').replace('1', '0').replace('a', '1')
    n = int(n, 2) + 1
    return n
print(f(95))