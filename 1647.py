import sys

read = sys.stdin.readline

N, M = map(int, read().split())

Edge = []
for i in range(M):
    Edge.append(list(map(int, read().split())))

Edge.sort(key=lambda x: x[2])
parents = [0] + [i for i in range(1, N + 1)]
rank = [0] + [1 for i in range(1, N + 1)]


def find(v):
    if v != parents[v]:
        parents[v] = find(parents[v])
    return parents[v]


def union(v1, v2, w):
    global cnt
    global sol
    root1, root2 = find(v1), find(v2)
    if root1 != root2:
        cnt += 1
        sol += w
        if rank[root1] < rank[root2]:
            parents[root1] = root2
            rank[root2] += rank[root1]
        else:
            parents[root2] = root1
            rank[root1] += rank[root2]


cnt = 0
sol = 0
for e in Edge:
    union(e[0], e[1], e[2])
    if cnt == N - 2:
        break
print(sol)