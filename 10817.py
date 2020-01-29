import sys

a, b, c = map(int, sys.stdin.readline().strip().split())
list = [a,b,c]
list.remove(max(list))
print(max(list))
