import sys

word = sys.stdin.readline().strip()
word_len = len(word)
bomb = sys.stdin.readline().strip()
bomb_len = len(bomb)
list = []
i = 0
check_len = 0
while i < word_len:
    list.append(word[i])
    check_len += 1
    i += 1
    if check_len >= bomb_len:
        for j in range(-1, -bomb_len - 1, -1):
            if list[j] != bomb[j]:
                break
        else:
            a = 0
            while a < bomb_len:
                list.pop()
                check_len -= 1
                a += 1

word = ''.join(list)

if len(word) == 0:
    print("FRULA")
else:
    print(word)
