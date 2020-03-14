import sys

n = int(sys.stdin.readline().strip())
if n % 7 == 2 or n % 7 == 0:
    print("CY")
else:
    print("SK")
