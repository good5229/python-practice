import sys

N, K = map(int, sys.stdin.readline().split())
dp = [1]
dp += [0] * N

for _ in range(1, K + 1):
    for idx in range(1, N + 1):
        dp[idx] = (dp[idx] + dp[idx - 1]) % 1000000000

sys.stdout.write(str(dp[N]))
