def fibonacci(z, n=100):
    fn = [0, 1]
    for i in range(2, n):
        x = fn[i-1] + fn[i-2]
        if x > z:
            return x
        fn.append(x)
def f(n, k):
    if n > k:
        return 0
    if n == k:
        return 1
    if n < k:
        return f(n + 1, k) + f(n + 4, k) + f(fibonacci(n), k)
print(f(1, 13)) 
