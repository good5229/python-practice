import sys

t = int(sys.stdin.readline().strip())
for i in range(t):
    command = sys.stdin.readline().strip()
    arr_len = int(sys.stdin.readline().strip())
    if (arr_len == 0):
        input_arr = sys.stdin.readline().split()
        input_arr = []
    else:
        input_arr = list(map(int, sys.stdin.readline().strip()[1:-1].split(',')))
    is_reverse = False
    is_ok = True
    front = 0
    back = 0
    for act in command:
        try:
            if act == 'R':
                is_reverse = not is_reverse
            elif act == 'D' and not is_reverse:
                front += 1
            elif act == 'D' and is_reverse:
                back += 1
        except:
            is_ok = False
            print('error')
            break
    if is_ok == True:
        if (front + back) <= arr_len:
            if not is_reverse:
                input_arr = input_arr[front:arr_len - back]
                print(str(input_arr).replace(' ', ''))
            else:
                input_arr = input_arr[::-1][back:arr_len - front]
                print(str(input_arr).replace(' ', ''))
        else:
            print('error')
