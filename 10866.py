import sys

n = int(sys.stdin.readline().strip())
cmd_list = []
for i in range(n):
    cmd = sys.stdin.readline().strip()
    # print(cmd_list)
    if cmd.startswith('push_back'):
        cmd_text, cmd_value = cmd.split()
        cmd_list.append(int(cmd_value))
    elif cmd.startswith('push_front'):
        cmd_text, cmd_value = cmd.split()
        cmd_list.insert(0, int(cmd_value))
    elif cmd.startswith('pop_front'):
        if len(cmd_list) < 1:
            print(-1)
        else:
            print(cmd_list[0])
            cmd_list.pop(0)
    elif cmd.startswith('pop_back'):
        if len(cmd_list) < 1:
            print(-1)
        else:
            print(cmd_list[-1])
            cmd_list.pop(-1)
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
