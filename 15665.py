import itertools
import sys

# 15665
n, k = map(int, sys.stdin.readline().split())
N_list = list(map(int, sys.stdin.readline().split()))
N_list = list(set(N_list))
N_list = sorted(N_list)

for numbers in list(itertools.product(N_list, repeat=k)):
    for num in numbers:
        print(num, end=' ')
    print()

# 15666
# n, k = map(int, sys.stdin.readline().split())
# N_list = list(map(int, sys.stdin.readline().split()))
# N_list = list(set(N_list))
# N_list = sorted(N_list)
#
# for numbers in list(itertools.combinations_with_replacement(N_list, k)):
#     for num in numbers:
#         print(num, end=' ')
#     print()