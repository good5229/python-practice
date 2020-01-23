import sys


def break_even():
    a, b, c = map(int, sys.stdin.readline().split())

    if c <= b:
        return -1
    else:
        n = a // (c - b) + 1
        return n


print(break_even())
