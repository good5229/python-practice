import sys


def basketball():
    n = sys.stdin.readline().strip()
    list = []
    for i in range(int(n)):
        name = sys.stdin.readline().strip()
        list.append(name)
    answer = []
    for i in range(int(n)):
        if list[i][0] in answer:
            continue
        else:
            count = 0
            for j in range(int(n)):
                word = list[i][0]
                if word in list[j][0]:
                    count = count + 1
            if count >= 5:
                answer.append(word)
    answer.sort()
    if len(answer) > 0:
        print(''.join(answer))
    else:
        print("PREDAJA")


basketball()
