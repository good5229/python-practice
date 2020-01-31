import sys


def f():
    n = int(sys.stdin.readline().strip())
    stack = []
    for i in range(n):
        cmd = sys.stdin.readline().strip()
        if 'push' in cmd:
            cmd, val = cmd.split()
            stack.append(int(val))
        elif 'top' in cmd:
            if len(stack) > 0:
                print(stack[-1])
            else:
                print(-1)
        elif 'size' in cmd:
            print(len(stack))
        elif 'empty' in cmd:
            if len(stack) > 0:
                print(0)
            else:
                print(1)
        elif 'pop' in cmd:
            if len(stack) > 0:
                print(stack[-1])
                stack.pop(len(stack) - 1)
            else:
                print(-1)


f()
