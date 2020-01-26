import sys


def hunter():
    n = int(sys.stdin.readline().strip())
    result = ""
    for i in range(n):
        a, b = map(int, sys.stdin.readline().split())
        prize = 0
        if a > 0:
            if a < 2:
                prize += 5000000
            elif a < 4:
                prize += 3000000
            elif a < 7:
                prize += 2000000
            elif a < 11:
                prize += 500000
            elif a < 16:
                prize += 300000
            elif a < 22:
                prize += 100000
        if b > 0:
            if b < 2:
                prize += 5120000
            elif b < 4:
                prize += 2560000
            elif b < 8:
                prize += 1280000
            elif b < 16:
                prize += 640000
            elif b < 32:
                prize += 320000
        result += f"{prize}\n"
    return result


print(hunter())
