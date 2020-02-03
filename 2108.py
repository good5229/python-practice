import sys
from collections import Counter

n = int(sys.stdin.readline().strip())
num_list = sorted([int(sys.stdin.readline().strip()) for _ in range(n)])

avg = round(sum(num_list) / len(num_list))
print(avg)

if n == 1:
    median = num_list[0]
else:
    median = num_list[n // 2]
print(median)

if n == 1:
    print(num_list[0])
else:
    c = Counter(num_list).most_common(2)
    print(c)
    if c[0][1] == c[1][1]:
        print(c[1][0])
    else:
        print(c[0][0])

print(num_list[-1] - num_list[0])


