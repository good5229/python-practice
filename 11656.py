import sys

word = sys.stdin.readline().strip()
arr = []
for i in range(len(word)):
    arr.append(word[i:len(word)])
arr = sorted(arr)
for s in arr:
    print(s)