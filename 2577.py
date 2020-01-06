def count_num(num_1, num_2, num_3):
    if num_1 < 100 or num_2 < 100 or num_3 < 100:
        print("100 이하의 숫자가 입력되었습니다.")
    elif num_1 >= 1000 or num_2 >= 1000 or num_3 >= 1000:
        print("1000 이상의 숫자가 입력되었습니다.")
    else:
        result = num_1 * num_2 * num_3
        count = [0 for i in range(10)]
        list = []
        for i in str(result):
            digit = int(i)
            count[digit] += 1
        for i in count:
            print(i)


num_1 = int(input(''))
num_2 = int(input(''))
num_3 = int(input(''))
count_num(num_1, num_2, num_3)
