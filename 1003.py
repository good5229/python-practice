import sys


def count_fibonacci(n):
    zero_count = [1, 0]
    one_count = [0, 1]
    if n <= 1:
        return

    for i in range(2, n + 1):
        zero_count.append(zero_count[i - 1] + zero_count[i - 2])
        one_count.append(one_count[i - 1] + one_count[i - 2])

    return zero_count, one_count


t = int(sys.stdin.readline().strip())
zero_count, one_count = count_fibonacci(40)

for i in range(t):
    m = int(sys.stdin.readline().strip())
    print("%d %d" % (zero_count[m], one_count[m]))
