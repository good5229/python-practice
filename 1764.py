import sys

n, m = map(int, sys.stdin.readline().split())
n_set = set()
m_set = set()
for i in range(n):
    name = sys.stdin.readline().strip()
    n_set.add(name)
for j in range(m):
    name = sys.stdin.readline().strip()
    m_set.add(name)

ans = sorted(list(n_set & m_set))
print(len(ans))
for word in ans:
    print(word)
