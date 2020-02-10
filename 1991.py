import sys


def preorder(tree, root):
    stack = list()
    stack.append(root)
    result = ''
    while 0 < len(stack):
        data = stack.pop()
        result += data

        if tree[data][1] != '.':
            stack.append(tree[data][1])
        if tree[data][0] != '.':
            stack.append(tree[data][0])
    print(result)


def inorder(tree, root):
    stack = list()
    stack.append(root)
    data = root
    result = ''
    while True:
        while tree[data][0] != '.':
            if data not in result:
                stack.append(tree[data][0])
                data = tree[data][0]
            else:
                break
        if 0 < len(stack):
            data = stack.pop()
            result += data
            if tree[data][1] != '.':
                stack.append(tree[data][1])
                data = tree[data][1]
        else:
            break
    print(result)


def postorder(tree, root):
    stack = list()
    stack.append(root)
    data = root
    result = ''
    while True:
        while tree[data][0] != '.':
            if tree[data][0] not in result:
                stack.append(tree[data][0])
                data = tree[data][0]
            else:
                break
        last_data = stack[-1]
        if tree[last_data][1] == '.':
            result += stack.pop()
            if stack:
                data = stack[-1]
            else:
                break
        else:
            if tree[data][1] not in result:
                stack.append(tree[data][1])
                data = tree[data][1]
            else:
                result+=stack.pop()
                if 0 < len(stack):
                    data = stack[-1]
                else:
                    break
    print(result)


def solve(tree, root):
    preorder(tree, root)
    inorder(tree, root)
    postorder(tree, root)


n = int(sys.stdin.readline().strip())

tree = {}
for i in range(n):
    info = sys.stdin.readline().split()
    tree[info[0]] = [info[1], info[2]]

solve(tree, 'A')
