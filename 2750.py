import sys


def sort():
    n = int(sys.stdin.readline().strip())
    list = [0] * 10001
    for i in range(n):
        x = int(sys.stdin.readline().strip())
        list[x] = list[x]+1
    for i in range(len(list)):
        if list[i] != 0:
            for j in range(list[i]):
                print(list[i])


sort()
