import sys

N = int(sys.stdin.readline())

# matrix = [0 for _ in range(N)] # Matrix size
matrix = []
mul = [[0] * N for _ in range(N)]
for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

if N == 1:
    print(0)
else:
    for i in range(1, N):
        for j in range(i):
            k = i - j - 1
            # func(i, k)
            min_mul = 2 ** 31 - 1
            t = 0

            if i - k == 1:
                mul[k][i] = matrix[k][0] * matrix[k][1] * matrix[i][1]
                continue
            while True:
                if k + t >= i:
                    break
                min_mul = min(min_mul,
                              mul[k][k + t] + mul[k + t + 1][i] + \
                              matrix[k][0] * matrix[k + t][1] * matrix[i][1])
                t += 1
            mul[k][i] = min_mul

    print(mul[0][N - 1])