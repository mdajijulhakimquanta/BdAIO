n, t = map(int, input().split())

k = list(map(int, input().split()))

lo, hi = 0, max(k) * t

while lo <= hi:
    mid = (lo + hi) // 2
    temp = sum(mid // x for x in k)
    if temp >= t:
        hi = mid - 1
    else:
        lo = mid + 1
        
print(lo)