import itertools
import sys

# 15663
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

# 15664
# n, k = map(int, sys.stdin.readline().split())
# arr = sorted(list(map(int, sys.stdin.readline().split())))
#
# output = []
# for s in itertools.combinations(arr, k):
#     output.append(s)
# output = sorted(list(set(output)))
#
# for numbers in output:
#     for num in numbers:
#         print(num, end=' ')
#     print()
