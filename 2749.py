import sys

# 메모리 초과!
# n = int(sys.stdin.readline().strip())
# fib = [0, 1, 1]
# i = 1
# if n <= 3:
#     print(fib[n-1])
# else:
#     while i < n-1:
#         fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
#         i += 1
#     print(fib[n] % 1000000)


# 파사노 주기 활용
n = int(sys.stdin.readline().strip())


def fibo3(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b % 1000000, (a + b) % 1000000

    return a


print(fibo3(n % (15 * (10 ** 5))))
