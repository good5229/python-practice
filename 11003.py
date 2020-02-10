import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
dq = deque()
for i in range(n):
    tmp = arr[i]

    while dq and dq[-1] > tmp:
        dq.pop()
    dq.append(tmp)

    if i >= m and dq[0] == arr[i - m]:
        dq.popleft()
    print(dq[0], end=' ')
