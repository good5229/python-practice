import sys

n = int(sys.stdin.readline().strip())
dot_list = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    dot_list.append((x, y))

dot_list.sort(key=lambda x: (x[0], x[1]))

for dots in dot_list:
    print(f'{dots[0]} {dots[1]}')
