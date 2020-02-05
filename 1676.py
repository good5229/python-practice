import sys


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


n = int(sys.stdin.readline().strip())
str_n = str(factorial(n))[::-1]

i = 0
count = 0

for i in str_n:
    if i == "0":
        count += 1
    else:
        break
print(count)
