def change_location(str):
    str = int(str[::-1])
    return str


def read_answer(num1, num2):
    sangsu_num1 = int(change_location(num1))
    sangsu_num2 = int(change_location(num2))
    return max(sangsu_num1, sangsu_num2)


a, b = input("").split()
print(read_answer(a, b))
