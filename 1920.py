import sys


def BinarySearch(arr, val, low, high):
    if low > high:
        return False

    mid = (low + high) // 2
    if arr[mid] > val:
        return BinarySearch(arr, val, low, mid - 1)
    elif arr[mid] < val:
        return BinarySearch(arr, val, mid + 1, high)
    else:
        return True


n = int(sys.stdin.readline().strip())
n_list = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())
m_list = list(map(int, sys.stdin.readline().split()))
n_list.sort()

for m_num in m_list:
    if BinarySearch(n_list, m_num, 0, n - 1):
        print(1)
    else:
        print(0)
