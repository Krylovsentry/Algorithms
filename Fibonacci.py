"""
Fibonacci numbers
"""


# Difficult growths by exp
def fib_recursion(n):
    if n < 2:
        return n

    return fib_recursion(n - 1) + fib_recursion(n - 2)


print(fib_recursion(1))


# Difficult O(n)
def fibonacci(n):
    number = [x for x in range(n + 1)]
    number[0] = 0
    number[1] = 1

    for i in range(2, n + 1):
        number[i] = number[i - 1] + number[i - 2]

    return number[n]


print(fibonacci(2222))
