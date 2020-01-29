import sys


def leftover():
    list = []
    for i in range(10):
        n = int(sys.stdin.readline().strip())
        list.append(n)
    s1 = set()
    for i in list:
        s1.add(i % 42)

    print(len(s1))

leftover()