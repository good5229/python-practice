import itertools
import sys

n, k = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))

output = []
for s in itertools.permutations(arr, k):
    output.append(s)
output = sorted(list(set(output)))

for numbers in output:
    for num in numbers:
        print(num, end=' ')
    print()