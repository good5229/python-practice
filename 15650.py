import itertools
import sys


def combination():
    n, m = sys.stdin.readline().split()
    share = []
    for i in range(1, int(n)+1):
        share.append(i)
    for s in itertools.combinations(share, int(m)):
        for j in range(len(s)):
            print(s[j], end=' ')
        print('')

combination()

