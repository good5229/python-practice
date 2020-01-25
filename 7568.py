import sys


def big():
    n = int(sys.stdin.readline().strip())
    list = []
    for i in range(n):
        w, h = map(int, sys.stdin.readline().split())
        list.append((w, h))

    for i in list:
        rank = 1
        for j in list:
            if i[0] < j[0] and i[1] < j[1]:
                rank += 1
        print(rank, end=' ')


big()

