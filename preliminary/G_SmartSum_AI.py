n = int(input())
coins = list(map(int, input().split()))

maximumAmount = sum(coins)

arr = [False] * (maximumAmount + 1)

arr[0] = True  

for coin in coins:
    for i in range(maximumAmount, coin - 1, -1):
        if arr[i - coin]:
            arr[i] = True
            
result = [i for i in range(1, maximumAmount + 1) if arr[i]]

print(len(result))

print(*result)

