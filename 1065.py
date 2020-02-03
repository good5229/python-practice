import sys

n = int(sys.stdin.readline().strip())
count = 0
for i in range(1, n + 1):
    str_i = str(i)
    if i <= 99:
        count += 1
    else:
        if int(str_i[0]) - int(str_i[1]) == int(str_i[1]) - int(str_i[2]):
            count += 1
print(count)
