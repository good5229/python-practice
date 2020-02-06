import sys


def find(node):
    global cnt
    if node.data == []:
        cnt += 1
    for data in node.data:
        find(tree[data])


class Tree:
    def __init__(self):
        self.data = []

    def setChild(self, node):
        self.data.append(node)

    def removeChild(self, node):
        self.data.remove(node)


n = int(sys.stdin.readline().strip())
tree = [Tree() for _ in range(n)]
cnt = 0
parent = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    if parent[i] != -1:
        tree[parent[i]].setChild(i)

if n != 1:
    i = int(sys.stdin.readline().strip())
    if parent[i] == -1:
        cnt = 0
    else:
        tree[parent[i]].removeChild(i)
        find(tree[parent.index(-1)])

print(cnt)