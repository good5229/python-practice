import sys


def snow():
    test_num = sys.stdin.readline().strip()
    text = ""
    for i in range(int(test_num)):
        row, column = sys.stdin.readline().split()
        if int(row) < 12 or int(column) < 4:
            text += "-1\n"
        else:
            k_max = int(column) * 11
            l4_seat = k_max + 4
            text += str(l4_seat) + "\n"
    print(text)


snow()

