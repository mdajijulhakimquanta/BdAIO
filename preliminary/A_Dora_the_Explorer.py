import math

def solve():
    t = int(input())
    for _ in range(t):
        m, n, d = map(int, input().split())
        relspeed = math.sqrt(m ** 2 + n ** 2)
        time_hours = d / relspeed
        time_minutes = time_hours * 60
        
        if abs(time_minutes - int(time_minutes)) < 1e-9:
            print(f"{int(time_minutes)}.0")
        else:
            print(f"{time_minutes:.6f}")
solve()
