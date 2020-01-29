import sys


def day():
    m, d = map(int, sys.stdin.readline().strip().split())
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    name_days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    i = 1
    j = 0
    while i < m:
        j += month_days[i - 1]
        i += 1
    total_day = j + d
    return name_days[(total_day % 7) - 1]


print(day())
