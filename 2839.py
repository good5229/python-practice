import sys


def calc_weight(num):
    box = 0
    while True:
        if (num % 5) == 0:
            box = box + (num // 5)
            return box
        num = num - 3
        box += 1
        if num < 0:
            return -1


weight = int(sys.stdin.readline().strip())
print(calc_weight(weight))
