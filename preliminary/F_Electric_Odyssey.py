n = int(input())
h = list(map(int, input().split()))

current = 0
minmumCharge = 0

for i in range(n - 1):
    defference = h[i + 1] - h[i]
    if defference > 0:
        current -= defference
    else:
        current += -defference
    if current < minmumCharge:
        minmumCharge = current

initialCharge = -minmumCharge
print(initialCharge)