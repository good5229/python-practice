import sys

parent = {}
rank = {}


def make_set(v):
    parent[v] = v
    rank[v] = 0


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])

    return parent[v]


def union(v, u):
    root1 = find(v)
    root2 = find(u)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1


def kruskal(graph):
    for v in graph['vertices']:
        make_set(v)

    mst = []

    edges = graph['edges']
    edges.sort()

    for edge in edges:
        weight, v, u = edge

        if find(v) != find(u):
            union(v, u)
            mst.append(edge)

    return mst


V, E = map(int, sys.stdin.readline().split())
graph = {
    'vertices': [str(i) for i in range(1, V + 1)],
    'edges': []
}
for i in range(E):
    A, B, C = sys.stdin.readline().split()
    graph['edges'].append((int(C), A, B))

ans = kruskal(graph)
sum_ = 0
for tuple_ in ans:
    sum_ += tuple_[0]

print(sum_)
