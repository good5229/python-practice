import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

sum_arr = [0] * (N + 1)
for i in range(1, N + 1):
    sum_arr[i] = sum_arr[i - 1] + arr[i - 1]

start = 0
end = 1
ans = 999999999  # 어처구니없는 값을 하나 넣어주자

while start != N:
    if sum_arr[end] - sum_arr[start] >= S:
        if end - start < ans:
            ans = end - start
        start += 1

    else:
        if end != N:
            end += 1
        else:
            start += 1

if ans != 999999999:
    print(ans)
else:
    print(0)