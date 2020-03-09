import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())

count = 0
for i in range(n):
    if arr[i] > 0:
        arr[i] -= b
        count += 1

    if arr[i] > 0:
        count += int(arr[i] / c)
        if arr[i] % c != 0:
            count += 1
print(count)

