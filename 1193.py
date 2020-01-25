import sys


def find():
    n = int(sys.stdin.readline().strip())
    sum = 1
    i = 2
    while n > sum:
        sum += i
        i += 1
    F = sum-n
    if n == 1:
        return "1/1"
    elif i % 2 == 1:
        return f"{i-F-1}/{F+1}"
    else:
        return f"{F+1}/{i-F-1}"


print(find())


