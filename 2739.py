import sys

n = int(sys.stdin.readline().strip())
if n >= 1 and n < 10:
    for i in range(1,10):
        print(f'{n} * {i} = {n*i}')
