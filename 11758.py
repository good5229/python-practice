import sys

x1, y1 = map(int, sys.stdin.readline().split())
x2, y2 = map(int, sys.stdin.readline().split())
x3, y3 = map(int, sys.stdin.readline().split())

temp = x1 * y2 + x2 * y3 + x3 * y1
temp -= y1 * x2 + y2 * x3 + y3 * x1
if temp > 0:
    print(1)
elif temp < 0:
    print(-1)
else:
    print(0)
