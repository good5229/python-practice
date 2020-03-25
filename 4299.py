import sys

input = sys.stdin.readline

x, y = map(int, input().split())
a = int((x + y) / 2)
b = int((x - y) / 2)

if ((x + y) % 2) != 0 or (x - y) % 2 != 0:
    print("-1")
else:
    if a >= 0 and b >= 0:
        if a >= b:
            print(f'{a} {b}')
        else:
            print(f'{b} {a}')
    else:
        print("-1")
