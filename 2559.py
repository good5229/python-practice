import sys

n, k = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
temp_sum = sum(num_list[0:k])
i = 0
max_sum = temp_sum
if k == 1:
    print(max(num_list))
else:
    while True:
        temp_sum -= num_list[i]
        if i + k >= n:
            break
        temp_sum += num_list[i + k]
        if max_sum < temp_sum:
            max_sum = temp_sum
        i += 1
    print(max_sum)
