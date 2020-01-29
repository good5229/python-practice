import sys


# def movie():
#     n = int(sys.stdin.readline().strip())
#     movie = 666
#     while n:
#         if "666" in str(movie):
#             n -= 1
#             movie += 1
#     print(movie - 1)
#
#
# print(movie())

def star():
    n = int(sys.stdin.readline().strip())
    for i in range(1, n + 1):
        print(' ' * (i - 1), end='')
        print('*' * (n - i + 1), end='')
        print('')


star()
