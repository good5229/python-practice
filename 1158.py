import sys

n,k=map(int, sys.stdin.readline().split())
arr = list(range(1,n+1))
ans = []
i = k-1
while True:
  ans.append(arr.pop(i))
  if not arr:
    break
  i = (i+k-1)%len(arr)
# print("answer",ans)
# print("array",arr, pointer, len(arr))

print('<'+', '.join(map(str, ans))+'>')