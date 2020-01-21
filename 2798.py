import itertools
import sys


def blackjack():
    n, m = sys.stdin.readline().strip().split()

    num = map(int, sys.stdin.readline().strip().split())

    max = 0
    for s in itertools.combinations(num, 3):
        if sum(s) <= int(m) and sum(s) > max:
            max = sum(s)

    return max


print(blackjack())
