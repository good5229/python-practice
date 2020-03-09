import sys
from itertools import permutations

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
plus, minus, multiple, div = map(int, sys.stdin.readline().split())

operation_list = []
operation_list += [1] * plus
operation_list += [2] * minus
operation_list += [3] * multiple
operation_list += [4] * div

operation_set = []
for numbers in list(permutations(operation_list)):
    operation_set.append(numbers)
operation_set = list(set(operation_set))

max_answer = -1000000001
min_answer = 1000000001
for case in operation_set:
    answer = arr[0]
    for i in range(n - 1):
        if case[i] == 1:
            answer += arr[i + 1]
        elif case[i] == 2:
            answer -= arr[i + 1]
        elif case[i] == 3:
            answer *= arr[i + 1]
        elif case[i] == 4:
            if answer < 0:
                answer = -(-answer // arr[i + 1])
            else:
                answer //= arr[i + 1]

    if answer < min_answer:
        min_answer = answer
    if answer > max_answer:
        max_answer = answer

print(max_answer)
print(min_answer)