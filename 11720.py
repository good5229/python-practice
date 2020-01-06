def sum():
    num = input('')  # 합할 숫자의 개수
    input_num = int(input(''))  # 합할 숫자들
    input_num_str = str(input_num)
    sum = 0
    for i in range(0, int(num)):
        sum += int(input_num_str[i])
    return sum

print(sum())
