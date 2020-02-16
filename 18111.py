import sys

n, m, b = map(int, sys.stdin.readline().split())
arr = []
max_height = 0
min_height = 999
time_result = 99999999
block_height = 99999999
for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    for j in row:
        if j > max_height:
            max_height = j
        if j < min_height:
            min_height = j
    arr.append(row)

for x in range(min_height, max_height + 1):
    time = 0
    block = b
    for N in range(n):
        for M in range(m):
            height = arr[N][M] - x
            if height > 0:
                time = time + height * 2
                block = block + height
            elif height < 0:
                time = time - height
                block = block + height
    if block >= 0:
        if time <= 9999999:
            time_result = time
            block_height = x

print(time_result, block_height)
