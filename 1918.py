import sys


def priority(x):
    if x == "*" or x == "/":
        return 2
    elif x == "+" or x == "-":
        return 1
    elif x == "(" or x == ")":
        return 0

    return -1


def solve():
    X = sys.stdin.readline().strip()

    ans = ""
    stack = []

    for c in X:

        p = priority(c)

        if c == '+' or c == '-' or c == '*' or c == '/':
            while stack and priority(stack[-1]) >= p:
                ans += stack.pop()
            stack.append(c)
            continue
        elif c == '(':
            stack.append(c)
            continue
        elif c == ')':
            while stack and stack[-1] != "(":
                ans += stack.pop()
            stack.pop()
            continue

        ans += c

    while stack:
        ans += stack.pop()
    print(ans)


solve()
