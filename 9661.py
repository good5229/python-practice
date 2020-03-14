import sys

n = int(sys.stdin.readline().strip())
if (n - 1) % 5 + 1 == 2 or (n - 1) % 5 + 1 == 5:
    print("CY")
else:
    print("SK")
