import sys

n = int(sys.stdin.readline().strip())
num_list = []
i = 2
while n > 1:
    if n % i == 0:
        n = n // i
        num_list.append(i)
        i = 2
    else:
        i += 1
for j in range(len(num_list)):
    print(num_list[j])
