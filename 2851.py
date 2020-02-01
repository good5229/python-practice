import sys

mushroom = []
for i in range(10):
    a = int(sys.stdin.readline().strip())
    mushroom.append(a)

result=0
for i in mushroom:
    pre = result
    result += i
    if result>=100:
        break

if abs(100-pre) == abs(100-result):
    if pre>result:
        print(pre)
    else:
        print(result)
else:
    if abs(100-pre) > abs(100-result):
        print(result)
    else:
        print(pre)