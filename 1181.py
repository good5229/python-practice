import sys

n = int(sys.stdin.readline().strip())
word = []
for k in range(n):
    e = sys.stdin.readline().strip()
    word.append((e, len(e)))

list_word = list(set(word))

list_word.sort(key=lambda x: (x[1], x[0]))

for i in range(len(list_word)):
    print(list_word[i][0])

