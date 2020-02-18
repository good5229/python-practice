import sys

N, M, K = map(int, sys.stdin.readline().split())

target = M
arr = [i for i in range(1, N + 1)]
n = 1
for i in range(1, N + 1):
    if M % (N - n + 1) == 0:
        nM = N - n + 1
    else:
        nM = M % (N - n + 1)
    if K == nM:
        break
    else:
        if K > nM:
            K = K - nM
        else:
            K = K - nM + N - n + 1
    n += 1

print(n)
