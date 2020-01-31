import sys

n = int(sys.stdin.readline().strip())
file = []
for i in range(n):
    word = sys.stdin.readline().strip()
    file.append(word)

same_word = file[0]
answer = []
file.pop(0)
borders = ''
j = ()
if n == 1:
    print(word)

for j in range(len(file)):
    if len(answer) < 1:
        for k in range(len(same_word)):
            if file[j][k] == same_word[k]:
                if len(answer) < len(same_word):
                    answer.append(file[j][k])
                else:
                    answer[k] = file[j][k]
            else:
                borders = file[j][k]
                end_text = "?"
                if len(answer) < len(same_word):
                    answer.append(end_text)
                else:
                    answer[k] = end_text
    else:
        for k in range(len(answer)):
            if file[j][k] != same_word[k]:
                borders = file[j][k]
                end_text = "?"
                answer[k] = end_text

print(''.join(answer))
