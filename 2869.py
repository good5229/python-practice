import sys


def snail():
    A, B, V = map(int, sys.stdin.readline().split())
    days = (V - B) / (A - B)

    if days == int(days):
        return int((V - B) / (A - B))
    else:
        return int(days) + 1


print(snail())

