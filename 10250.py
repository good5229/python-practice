import sys


def hotel():
    n = sys.stdin.readline().strip()
    result = ""
    for i in range(int(n)):
        H, W, N = map(int, sys.stdin.readline().split())
        floor = N % H
        room_no = N // H + 1
        if floor == 0:
            floor = H
            room_no -= 1

        if room_no < 10:
            room_no = "0" + str(room_no)
        result += f"{floor}{room_no}\n"
    return result


print(hotel())

