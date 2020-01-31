import sys

n = int(sys.stdin.readline().strip())
time = list(map(int, sys.stdin.readline().split()))
time.sort()
sum_time = 0
previous = 0
total = 0
for i in range(len(time)):
    previous = sum_time
    sum_time += time[i]
    total += sum_time

print(total)
