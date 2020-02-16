import sys
from collections import deque


def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True
    cnt = 0

    while q:
        v = q.popleft()
        for e in adj[v]:
            if not visited[e]:
                visited[e] = True
                q.append(e)
                cnt += 1
    return cnt


V = int(sys.stdin.readline().strip())
E = int(sys.stdin.readline().strip())
adj = [[] for _ in range(V + 1)]
visited = [False for _ in range(V + 1)]
for _ in range(E):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)
print(bfs(1))
