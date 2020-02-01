import sys

word = ''
word_list = []
while True:
    word = sys.stdin.readline().strip()
    if word == 'END':
        break
    word_list.append(word)

for i in word_list:
    l = list(i.split())
    l.reverse()
    for j in l:
        print(j[::-1], end=' ')
    print('')
