import sys
from collections import deque


def bfs(graph, start):
    for i in graph:
        graph[i].sort()
    track_list = [start]
    visit = set()
    visit.add(start)
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node in graph:
            for w in graph[node]:
                if w not in visit:
                    visit.add(w)
                    track_list.append(w)
                    queue.append(w)
    return track_list


def dfs(graph, start):
    for i in graph:
        graph[i].sort(reverse=True)
    track_list = list()
    visit = set()
    stack = deque([start])
    while stack:
        node = stack.pop()
        if node in visit:
            continue
        visit.add(node)
        track_list.append(node)

        if node in graph:
            for w in graph[node]:
                if w not in visit:
                    stack.append(w)
    return track_list


N, M, V = map(int, sys.stdin.readline().split())
graph = {}
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]
    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]

print(*dfs(graph, V))
print(*bfs(graph, V))

# dfs_result = dfs(graph, V)
# for node in dfs_result:
#     print(node, end=' ')
# print('')
# bfs_result = bfs(graph, V)
# for bfs_node in bfs_result:
#     print(bfs_node, end=' ')
