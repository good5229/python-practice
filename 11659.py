import sys

n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
sum_list = []
sum_list.append(0)
sum_x = 0
for number in num_list:
    sum_x += number
    sum_list.append(sum_x)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(sum_list[b] - sum_list[a - 1])
