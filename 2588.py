import sys


def multiply():
    a = int(sys.stdin.readline().strip())
    b = int(sys.stdin.readline().strip())
    b_one = b % 10
    b_ten = (b % 100 - b_one) / 10
    b_hund = b // 100
    c = a * b_one
    d = int(a * b_ten)
    e = a * b_hund
    result = a * b
    print(c)
    print(d)
    print(e)
    print(result)


multiply()
