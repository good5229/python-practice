import sys

n, q = map(int, sys.stdin.readline().split())
name = []
index = {}
for i in range(n):
    pk = sys.stdin.readline().strip()
    name.append(pk)
    index[pk] = i + 1

for j in range(q):
    question = sys.stdin.readline().strip()
    if question.isdigit():
        print(name[int(question) - 1])
    else:
        print(index[question])
