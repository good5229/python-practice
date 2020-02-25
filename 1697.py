import sys
from collections import deque


def bfs():
    q = deque()
    q.append(N)
    while q:
        v = q.popleft()
        if v == K:
            print(time[v])
            return
        for next_step in (v - 1, v + 1, v * 2):
            if 0 <= next_step < 100001 and not time[next_step]:
                time[next_step] = time[v] + 1
                q.append(next_step)


N, K = map(int, sys.stdin.readline().split())
time = [0] * 100001
bfs()

