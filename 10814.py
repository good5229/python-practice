import sys

n = int(sys.stdin.readline().strip())
member = []
order = 0
for i in range(n):
    age, name = sys.stdin.readline().split()
    age = int(age)
    order += 1
    member.append((age, name, order))

member.sort(key=lambda x: (x[0], x[2]))
for i in range(len(member)):
    print(member[i][0], member[i][1])
