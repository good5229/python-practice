import sys

list = []
for i in range(5):
    score = int(sys.stdin.readline().strip())
    if score < 40:
        score = 40
    list.append(score)
print(int(sum(list) / len(list)))
