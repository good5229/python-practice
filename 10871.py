import sys

n, x = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

for i in range(len(num_list)):
    if num_list[i] < x:
        print(num_list[i], end=' ')
