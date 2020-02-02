import sys


def movie():
    n = int(sys.stdin.readline().strip())
    count = 0
    v = 0
    while True:
        if '666' in str(v):
            count += 1
        if count == n:
            break
        v += 1
    return v

print(movie())

