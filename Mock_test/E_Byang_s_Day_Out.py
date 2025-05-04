def is_watch_match(a, b, c):
    if (a + b >= c) and (a + c >= b) and (b + c >= a):
        return "Yes"
    else:
        return "No"

T = int(input())
for i in range(T):
    a, b, c = map(int, input().split())
    print(is_watch_match(a, b, c))