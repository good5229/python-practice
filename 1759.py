import itertools
import sys

L, C = map(int, sys.stdin.readline().split())
arr = sorted(list(map(str, sys.stdin.readline().split())))
for s in itertools.combinations(arr, L):
    count = 0
    for letter in s:
        if letter in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    if 1 <= count <= L - 2:
        print(''.join(s))
