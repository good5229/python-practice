import sys

n = int(sys.stdin.readline().strip())
arr = [0, 1]


def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


for i in range(2, n + 1):
    arr.append(i)
    swap(arr, i, i - 1)
    j = i - 1
    while j != 1:
        swap(arr, j, j // 2)
        j = j // 2

for i in arr[1:]:
    print(i, end=' ')
