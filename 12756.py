import sys

one_att, one_life = map(int, sys.stdin.readline().split())
two_att, two_life = map(int, sys.stdin.readline().split())

while one_life > 0 and two_life > 0:
    one_life -= two_att
    two_life -= one_att

if one_life <= 0 and two_life <= 0:
    print("DRAW")
elif two_life <= 0 < one_life:
    print("PLAYER A")
elif one_life <= 0 < two_life:
    print("PLAYER B")