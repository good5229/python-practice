import sys

L = int(sys.stdin.readline().strip())
A = int(sys.stdin.readline().strip())
B = int(sys.stdin.readline().strip())
C = int(sys.stdin.readline().strip())
D = int(sys.stdin.readline().strip())

workday = 0
language_workday = 0
math_worday = 0
if (A % C) != 0:
    language_workday = (A // C) + 1
else:
    language_workday = (A // C)
if (B % D) != 0:
    math_worday = (B // D) + 1
else:
    math_worday = (B // D)
workday = max(language_workday, math_worday)
print(f'{L-workday}')
