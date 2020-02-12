import sys

n = int(sys.stdin.readline().strip())
company = set()
for i in range(n):
    name, status = sys.stdin.readline().split()
    if status == "enter":
        company.add(name)
    elif status == 'leave':
        company.remove(name)
company = sorted(list(company), reverse=True)
for worker in company:
    print(worker)
