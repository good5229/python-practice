import sys


T = int(sys.stdin.readline().strip())
results = []

for _ in range(T):
    a, b = map(int, sys.stdin.readline().strip().split())
    if a % 10 == 0: results.append(10)
    else:
        focus = 4 + b % 4
        data = str(a ** focus)
        results.append(data[-1])

for result in results:
    print(result)
