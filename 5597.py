import sys

students = [i for i in range(1, 31)]
for i in range(28):
    n = int(sys.stdin.readline().strip())
    students.remove(n)
print(min(students))
print(max(students))
