import decimal
import sys
decimal.getcontext().prec = 10000
n1, n2 = sys.stdin.readline().split()
print("{0:f}".format(decimal.Decimal(n1)**int(n2)))