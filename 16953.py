import sys

n, m = map(int, sys.stdin.readline().split())
count = 0
while True:
    if n > m:
        count = -1
        break
    if n == m:
        count += 1
        break
    if m % 2 == 0:
        m = m // 2
        count += 1
    else:
        if m % 10 == 1:
            m = str(m)[:-1]
            m = int(m)
            count += 1
        else:
            count = -1
            break

print(count)
