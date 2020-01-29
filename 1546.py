import sys


def avg():
    n = int(sys.stdin.readline().strip())
    text = ""
    for i in range(n):
        score_list = list(map(int, sys.stdin.readline().split()))
        amount = score_list[0]
        score_list.pop(0)
        average = sum(score_list) / amount
        count = 0
        for j in range(len(score_list)):
            if score_list[j] > average:
                count += 1
        s = count / amount * 100
        text += '%.3f%%\n' %s
    return text


print(avg())

