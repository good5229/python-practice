import sys

n, k = map(int, sys.stdin.readline().split())

money_list = []
b = 0
for i in range(n):
    m = int(sys.stdin.readline().strip())
    money_list.append(m)

for i in range(len(money_list)):
    if max(money_list) <= k:
        b = len(money_list) - 1
        break
    elif money_list[i] >= k:
        b = i - 1
        break

count = 0
while k > 0:
    count += k // money_list[b]
    k = k % money_list[b]
    b -= 1

print(count)

