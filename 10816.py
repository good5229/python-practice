import sys

n = int(sys.stdin.readline().strip())
n_list = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())
m_list = list(map(int, sys.stdin.readline().split()))

n_count = {}

for N in n_list:
    try:
        n_count[N] += 1
    except:
        n_count[N] = 1

ans = []
for M in m_list:
    try:
        ans.append(n_count[M])
    except:
        ans.append(0)

for i in ans:
    print(i, end=' ')
