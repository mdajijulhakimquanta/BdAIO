def solve(n, a):
    h = max(a[i] - i for i in range(n))

    counter = 0
    for i in range(n):
        height = h + i
        if height > a[i]:
            counter += height - a[i]
    return counter

n = int(input())
a = list(map(int, input().split()))

print(solve(n, a))
