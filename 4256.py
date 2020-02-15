import sys


def postorder(s, e, r):
    for i in range(s, e):
        if in_order[i] == pre_order[r]:
            postorder(s, i, r + 1)
            postorder(i + 1, e, r + i - s + 1)
            print(pre_order[r], end=' ')
            return


n = int(sys.stdin.readline().strip())
for i in range(n):
    length = int(sys.stdin.readline().strip())
    pre_order = list(map(int, sys.stdin.readline().split()))
    in_order = list(map(int, sys.stdin.readline().split()))
    postorder(0, length, 0)
    print("")
