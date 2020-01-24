import sys


def dial():
    word = sys.stdin.readline().strip().upper()
    time = 0
    for i in word:
        if i in "ABC":
            time += 2
        elif i in "DEF":
            time += 3
        elif i in "GHI":
            time += 4
        elif i in "JKL":
            time += 5
        elif i in "MNO":
            time += 6
        elif i in "PQRS":
            time += 7
        elif i in "TUV":
            time += 8
        elif i in "WXYZ":
            time += 9
    time += len(word)
    return time


print(dial())

