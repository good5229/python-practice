import re
import sys

n = sys.stdin.readline().strip()

p = re.compile('^(100+1+|01)+$')
a = p.match(str(n))
if a == None:
    print("NOISE")
else:
    if a.end() == len(n):
        print("SUBMARINE")
    else:
        print("NOISE")

