def fibonacci(n):
    fn = [0, 1]
    for i in range(2, n):
        fn.append(fn[i-1] + fn[i-2])
    return fn
fib = fibonacci(21)
def f(n, k):
    if n > k:
        return 0
    if n == k:
        return 1
    if n < k:
        return f(n + 1, k) + f(n + 3, k) + f(fib[n], k)
print(f(6, 21)) 