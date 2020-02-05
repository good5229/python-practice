import sys

N = int(sys.stdin.readline().strip())

dic = {}

for i in range(N):
    a = int(sys.stdin.readline().strip())
    if a in dic:
        dic[a] = dic[a] + 1
    else:
        dic[a] = 1

for sorted in sorted(dic.items()):
    for j in range(sorted[1]):
        print(sorted[0])
