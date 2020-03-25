import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
stack = [0]
result = [-1 for i in range(n)]

i = 1
while stack and i < n:
    while stack and arr[stack[-1]] < arr[i]:
        result[stack[-1]] = arr[i]
        stack.pop()
    stack.append(i)
    i += 1

print(*result)
