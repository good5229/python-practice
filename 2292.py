import sys


def honeycomb():
    n = sys.stdin.readline().strip()
    if int(n) == 1:
        return 1
    else:
        sum = 0
        count = 0
        while int(n) > sum:
            sum += count * 6
            count += 1
            if int(n) <= sum + 1:
                return count
                break


print(honeycomb())

