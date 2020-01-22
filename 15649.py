# 백트래킹 문제
import itertools
import sys


def func():
    n, m = sys.stdin.readline().split()
    state = []
    for i in range(1, int(n) + 1):
        state.append(int(i))
    for s in itertools.permutations(state, int(m)):
        for j in range(len(s)):
            print(s[j], end=' ')
        print('')


func()


