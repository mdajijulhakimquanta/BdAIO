def fib(n):
    n=int(n)
    if n <= 2: return 1
    else: return fib(n-1)+fib(n-2)
number=int(input())
print(fib(number))