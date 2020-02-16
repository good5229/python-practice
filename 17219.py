import sys

n, m = map(int, sys.stdin.readline().split())
arr = {}
ans = ""
for i in range(n):
    site, pw = sys.stdin.readline().split()
    arr[site] = pw
for j in range(m):
    site = sys.stdin.readline().strip()
    ans += arr[site] + "\n"
print(ans)

