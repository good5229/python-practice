import itertools
import sys

n = int(sys.stdin.readline().strip())
state = [i for i in range(1, n + 1)]
for s in itertools.permutations(state, n):
    s = list(s)
    for j in s:
        print(j, end=' ')
    print('')
