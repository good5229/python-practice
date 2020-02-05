import sys


def made_one():
    n = int(sys.stdin.readline().strip()) + 1
    count = [-1 for i in range(n)]

    for i in range(1, n):
        count[i] = count[i - 1] + 1
        if i % 2 == 0:
            count[i] = min([count[i], count[int(i / 2)] + 1])
        if i % 3 == 0:
            count[i] = min([count[i], count[int(i / 3)] + 1])

    return count[-1]


print(made_one())

# 1 -> 0
# 2 -> 1
# 3 -> 0
# 4 -> 1
# 5 -> 4
