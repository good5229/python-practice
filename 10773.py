import sys

k = int(sys.stdin.readline().strip())
num_list = []
for i in range(k):
    num = int(sys.stdin.readline().strip())
    if num != 0:
        num_list.append(num)
    else:
        num_list.pop(len(num_list) - 1)
print(sum(num_list))
