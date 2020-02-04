import sys

n = int(sys.stdin.readline().strip())
num_list = list(map(int, sys.stdin.readline().split()))
count = 0
for number in num_list:
    if number == 1:
        continue
    elif number == 2:
        count += 1
    else:
        for i in range(2, number):
            if number % i != 0 and number % number == 0:
                if i == number - 1:
                    count += 1
            else:
                break

print(count)
