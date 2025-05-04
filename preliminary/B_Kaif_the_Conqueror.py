from collections import deque

def solve():
    m, n, k = map(int, input().split())
    box = []
    q = deque()
    openBox = 0
    for i in range(m):
        row = list(map(int, input().split()))
        box.append(row)
        for j in range(n):
            if row[j] == 2:
                q.append((i, j, 0))
            elif row[j] == 1:
                openBox += 1
    
    if openBox == 0:
        print(1, 0)
        return
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    conquered = 0
    Updating_status = {}
    max_day = 0
    
    while q:
        x, y, day = q.popleft()
        if day > max_day:
            max_day = day
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and box[nx][ny] == 1:
                box[nx][ny] = 2
                conquered += 1
                next_day = day + 1
                q.append((nx, ny, next_day))
                if next_day in Updating_status:
                    Updating_status[next_day] += 1
                else:
                    Updating_status[next_day] = 1
    
    if conquered != openBox:
        print(0)
    else:
        if k in Updating_status:
            print(1, Updating_status[k])
        else:
            print(1, 0)

solve()