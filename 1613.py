import sys

# submit with pypy3

n, m = map(int, sys.stdin.readline().split())
Max = 9999999
S = [[Max] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    S[a][b] = 1

for k in range(n + 1):
    for i in range(n + 1):
        for j in range(n + 1):
            S[i][j] = min(S[i][j], S[k][j] + S[i][k])

for i in range(int(input())):
    a, b = map(int, input().split())
    if S[a][b] != Max:
        print(-1)
    elif S[b][a] != Max:
        print(1)
    else:
        print(0)
