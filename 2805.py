import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
start, end = 1, max(arr)


def summation(arr, cut):
    res = 0
    for tree in arr:
        if cut > tree:
            continue
        res += tree - cut
    return res


while True:
    mid = (start + end) // 2
    res = summation(arr, mid)
    if res == M:
        print(mid)
        exit()
    if end - 1 <= start:
        break
    elif res > M:
        start = mid
    else:
        end = mid
print(mid)
