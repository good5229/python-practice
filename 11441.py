import sys

n = int(sys.stdin.readline().strip())
num_list = list(map(int, sys.stdin.readline().split()))
sum_list = []
sum_list.append(0)
sum_total = 0
for number in num_list:
    sum_total += number
    sum_list.append(sum_total)

x = int(sys.stdin.readline().strip())
for i in range(x):
    a, b = map(int, sys.stdin.readline().split())
    print(sum_list[b] - sum_list[a - 1])

