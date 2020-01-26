import sys


def sort():
    n = int(sys.stdin.readline().strip())
    list = []
    for i in range(n):
        x = int(sys.stdin.readline().strip())
        list.append(x)
    list.sort()
    for i in range(n):
        print(list[i])


sort()
