# 전략
# 1. 2부터 sqrt(4000000)인 2000까지의 수 중 소수를 찾아 arr에 삽입한다.
# 2. 리스트의 처음부터 arr의 부분합을 계산한 sum_arr을 만든다
# 3. sum_arr에서 투포인터를 활용해서 연속된 부분집합의 합이 입력받은 수와 같으면 answer를 하나씩 늘려준다.
# 4. answer를 출력한다.

import sys

n = int(sys.stdin.readline().strip())

# 1
prime_ox = [True for _ in range(4000001)]

for i in range(2, int(4000001 ** 0.5)):
    if prime_ox[i]:
        for j in range(i + i, 4000001, i):
            prime_ox[j] = False
arr = [i for i, j in enumerate(prime_ox) if j == True and i >= 2]

# 2
sum_arr = [0] * (len(arr) + 1)
for i in range(1, len(arr) + 1):
    sum_arr[i] = sum_arr[i - 1] + arr[i - 1]

# 3
start = 0
end = 1
answer = 0
while start < len(sum_arr) and arr[end - 1] <= n:
    if sum_arr[end] - sum_arr[start] == n:
        answer += 1
        start += 1
    elif sum_arr[end] - sum_arr[start] > n:
        start += 1
    else:
        if end < len(sum_arr) - 1:
            end += 1
        else:
            start += 1
# 4
print(answer)
