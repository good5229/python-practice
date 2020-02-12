import sys

n = int(sys.stdin.readline().strip())
for i in range(n):
    amount = int(sys.stdin.readline().strip())
    list = {}
    sum = 1
    for j in range(amount):
        a, b = sys.stdin.readline().split()
        if not b in list:
            list[b] = 1
        else:
            list[b] += 1
    for k in list.keys():
        sum = sum * (list[k] + 1)
    print(sum - 1)
