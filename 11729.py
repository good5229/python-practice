import sys


def moveDisks(n, start, mid, end):
    if n == 1:
        print(start, end)
    else:
        moveDisks(n - 1, start, end, mid)
        print(start, end)
        moveDisks(n - 1, mid, start, end)


n = int(sys.stdin.readline().strip())
total_mvmt = 0
for disk in range(n):
    total_mvmt = total_mvmt * 2
    total_mvmt += 1

print(total_mvmt)
moveDisks(n, "1", "2", "3")