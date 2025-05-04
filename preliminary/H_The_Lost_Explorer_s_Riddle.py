from collections import deque

def solve():
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        adjency = [[] for _ in range(n + 1)]
        for _ in range(m):
            u, v = map(int, input().split())
            adjency[u].append(v)
            adjency[v].append(u)
        
        visited = [False] * (n + 1)
        Cycle = False
        
        for i in range(1, n + 1):
            if not visited[i]:
                queue = deque()
                queue.append((i, -1))
                visited[i] = True
                while queue and not Cycle:
                    u, parent = queue.popleft()
                    for v in adjency[u]:
                        if not visited[v]:
                            visited[v] = True
                            queue.append((v, u))
                        elif v != parent:
                            Cycle = True
                            break
                    if Cycle:
                        break
            if Cycle:
                break
        
        print("YES" if Cycle else "NO")

solve()
