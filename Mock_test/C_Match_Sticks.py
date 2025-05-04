import sys

for line in sys.stdin:
    N = int(line.strip())
    if (N - 2) % 3 == 0 and (N - 2) // 3 >= 1:
        print("Yes")
    else:
        print("No")