import sys

n = int(sys.stdin.readline().strip())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().strip()))

arr = sorted(arr)
ans = 0

for i in range(n - 2):
    ans = max(ans, abs(arr[n - 1] + arr[i] - arr[i + 1] * 2))
for i in range(1, n - 1):
    ans = max(ans, abs(-arr[0] + arr[i] * 2 - arr[i + 1]))
print(ans)
