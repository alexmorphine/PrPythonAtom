def fib(n):
    if n in (0, 1):
        return n
    if n >= 2:
        fibonachi = fib(n - 1) + fib(n - 2)
    return fibonachi