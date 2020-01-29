import sys


def avg():
    n = int(sys.stdin.readline().strip())
    old_score = list(map(int, sys.stdin.readline().split()))
    new_score = []
    m = max(old_score)
    for i in range(len(old_score)):
        change= old_score[i]*100/m
        new_score.append(change)
    return sum(new_score)/n


print(avg())