import sys

n = int(sys.stdin.readline().strip())
sum_list = [1, 2, 4]
for i in range(4, 11):
    sum_list.append(sum(sum_list[-3:]))
for j in range(n):
    num = int(sys.stdin.readline().strip())
    print(sum_list[num - 1])
