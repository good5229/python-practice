import sys

n = int(sys.stdin.readline().strip())
for _ in range(n):
    N = int(sys.stdin.readline().strip())

    while N <= 1000000000000000000:
        sum_digit = 0  # 자릿수의 합
        temp = N

        # 자릿수를 구하는 함수
        while temp != 0:
            sum_digit += temp % 10
            temp = temp // 10

        if sum_digit % 2 == 1:
            print(N)
            break

        else:
            N += N  # 다음 배수