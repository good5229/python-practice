import sys

n, m = map(int, sys.stdin.readline().split())
list_n = list(map(int, sys.stdin.readline().split()))
list_m = list(map(int, sys.stdin.readline().split()))
list_sort = sorted(list_n+list_m)
for i in list_sort:
    print(i, end=' ')
