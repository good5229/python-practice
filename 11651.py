def get_dots(num):
    list = []
    for i in range(num):
        x, y = input('').split()  # 점의 x,y좌표 입력
        list.append([int(x), int(y)])
    print(list)
    return list


def align_dots(list):
    x = list.sort(key=list[i][1])
    return x


num = int(input(''))  # 입력할 점의 갯수 입력

print(align_dots(get_dots(num)))
