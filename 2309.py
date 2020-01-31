import itertools
import sys


def f():
    dwarf = []
    for i in range(9):
        n = int(sys.stdin.readline().strip())
        dwarf.append(n)
    ans = []
    for s in itertools.permutations(dwarf, 7):
        if sum(s) == 100:
            for j in range(len(s)):
                ans.append(s[j])
            break
    ans.sort()
    for i in ans:
        print(i)


f()
