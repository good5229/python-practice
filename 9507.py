import sys

n = int(sys.stdin.readline().strip())
arr = [0 for i in range(68)]
arr[0] = arr[1] = 1
arr[2] = 2
arr[3] = 4

for number in range(4, len(arr)):
    arr[number] = arr[number - 1] + arr[number - 2] + arr[number - 3] + arr[number - 4]

for i in range(n):
    number = int(sys.stdin.readline().strip())
    print(arr[number])
