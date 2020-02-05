import sys

n = int(sys.stdin.readline().strip())
cmd_list = []
for i in range(n):
    cmd = sys.stdin.readline().strip()
    if cmd.startswith("push"):
        cmd_text, cmd_value = cmd.split()
        cmd_list.append(int(cmd_value))
    elif cmd.startswith("pop"):
        if len(cmd_list) < 1:
            print(-1)
        else:
            print(cmd_list[0])
            cmd_list.pop(0)
    elif cmd.startswith('size'):
        print(len(cmd_list))
    elif cmd.startswith('empty'):
        if len(cmd_list) > 0:
            print(0)
        else:
            print(1)
    elif cmd.startswith('front'):
        if len(cmd_list) > 0:
            print(cmd_list[0])
        else:
            print(-1)
    elif cmd.startswith('back'):
        if len(cmd_list) > 0:
            print(cmd_list[-1])
        else:
            print(-1)
