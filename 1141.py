import sys

n = int(sys.stdin.readline().strip())
words = []                  # 단어들
for i in range(n):
    words.append(sys.stdin.readline().rstrip())

words.sort()
cnt = n

for i in range(n):
    for j in range(i+1, n):
        if words[j].startswith(words[i]):
            cnt -= 1
            break

print(cnt)