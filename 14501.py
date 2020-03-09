import sys

n = int(sys.stdin.readline().strip())
time = [0 for _ in range(n)]
pay = [0 for _ in range(n)]
max_pay = [0 for _ in range(n)]
for i in range(n):
    time_input, pay_input = map(int, sys.stdin.readline().split())
    time[i] = time_input
    pay[i] = pay_input
    max_pay[i] = pay_input

max_pay.append(0)
for i in range(n - 1, -1, -1):
    if time[i] + i > n:
        max_pay[i] = max_pay[i + 1]
    else:
        max_pay[i] = max(max_pay[i + 1], pay[i] + max_pay[i + time[i]])

print(max_pay[0])

