import sys

n = int(sys.stdin.readline().strip())
a = []
x = list(map(int, sys.stdin.readline().split()))
for i in range(len(x)):
    a.append(x[i])

a = sorted(list(set(a)))
for num in a:
    print(num, end=' ')
