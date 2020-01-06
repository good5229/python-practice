import sys


def find_groupword():
    num = int(sys.stdin.readline().strip())  # 입력받을 단어의 수
    groupword_count = 0

    for i in range(num):
        word = input()
        for j in range(len(word)):
            if j != len(word) - 1:
                if word[j] == word[j + 1]:
                    pass
                elif word[j] in word[j + 1:]:
                    break
            else:
                groupword_count += 1
    return groupword_count


print(find_groupword())

