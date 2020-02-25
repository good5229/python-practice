import sys

c, a, b = map(int, sys.stdin.readline().split())
an = str(bin(a))[2:]
bn = str(bin(b))[2:]

length = 0
if len(an) > len(bn):
    length = len(an)
    bn = '0' * (length - len(bn)) + bn
else:
    length = len(bn)
    an = '0' * (length - len(an)) + an

r = ''
for i in range(length):
    r += an[i] + bn[i]
sys.stdout.write(str(int(r, 2)))