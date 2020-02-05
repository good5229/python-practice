import sys

testcase = int(sys.stdin.readline().strip())

for i in range(testcase):
    k = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    arr = [j for j in range(1,n+1)]
    for l in range(k):
        for j in range(n - 1):
            arr[j + 1] += arr[j]
        # arr(list)
    print(arr[-1])
