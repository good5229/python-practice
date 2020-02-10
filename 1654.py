import sys

k, n = map(int, sys.stdin.readline().split())
arr = list()
for i in range(k):
    num = int(sys.stdin.readline().strip())
    arr.append(num)
arr = sorted(arr)
start, end = 1, max(arr)
while start <= end:
    mid = (start + end) // 2
    line = 0
    for i in arr:
        line += i // mid
    if line >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)
