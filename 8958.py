import sys


def score():
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        record = sys.stdin.readline().strip()
        score = 0
        additional = 0
        for i in record:
            if i == "O":
                score += 1 + additional
                additional += 1
            else:
                additional = 0
        print(score)


score()


