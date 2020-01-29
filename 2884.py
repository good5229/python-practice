import sys


def alarm():
    h, m = map(int, sys.stdin.readline().split())
    if m >= 45:
        print(f'{h} {m-45}')
    else:
        if h == 0:
            h = 24
        print(f'{h-1} {m+15}')


alarm()

