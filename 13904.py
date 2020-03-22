import sys

n = int(sys.stdin.readline().strip())
arr = []
for i in range(n):
    d, w = map(int, sys.stdin.readline().split())
    arr.append((d, w))

arr = sorted(arr, key=lambda x: (-x[1], x[0]))
maxScore = 0
score = [0 for i in range(1001)]
for i in range(len(arr)):
    j = arr[i][0]
    for j in range(j, 0, -1):
        if score[j] == 0:
            score[j] = arr[i][1]
            break

for i in range(len(score)):
    maxScore += score[i]

print(maxScore)
