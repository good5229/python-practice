import sys

n = int(sys.stdin.readline().strip())
for i in range(n):
    n_list = sorted(list(map(int, sys.stdin.readline().split())))
    print(n_list[-3])
