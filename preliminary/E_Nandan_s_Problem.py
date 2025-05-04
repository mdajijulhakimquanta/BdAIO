import math

a, b, x, y = map(int, input().split())
gcd = math.gcd(x, y)
x //= gcd
y //= gcd

width= a // x
height = b // y

print(min(width, height))
