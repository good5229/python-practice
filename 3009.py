import sys


def rectangle():
    x_list = []
    y_list = []
    for i in range(3):
        x, y = map(int, sys.stdin.readline().split())
        x_list.append(x)
        y_list.append(y)

    if x_list[0] == x_list[1]:
        x_value = x_list[2]
    elif x_list[1] == x_list[2]:
        x_value = x_list[0]
    else:
        x_value = x_list[1]

    if y_list[0] == y_list[1]:
        y_value = y_list[2]
    elif y_list[1] == y_list[2]:
        y_value = y_list[0]
    else:
        y_value = y_list[1]
    print(f"{x_value} {y_value}")


rectangle()
