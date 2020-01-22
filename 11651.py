### 전략
# 1. 입력할 점의 갯수를 n으로 받는다
# 2. n번만큼 점의 좌표를 받고, 받은 좌표값만큼 list에 append한다.
# 3. for 문을 돌면서, y값이 최소인 점을 찾는다.
# 3-1. 최소인 점이 하나라면, answer list에 해당 점의 좌표를 append한다.
# 3-2. 최소인 점이 하나 이상이라면, 해당 점들 중 x값이 가장 작은 좌표를 append한다.
# 4. 3번 과정을 n번만큼 반복한다.
# 5. answer list를 append한다.

import sys


def dot_solve(n):
    list = []
    for i in range(int(n)):
        x, y = map(int, sys.stdin.readline().split())
        list.append([x, y])

    list.sort(key=lambda x: (x[1], x[0]))
    for i in list:
        print(i[0], i[1])


n = sys.stdin.readline().strip()
dot_solve(n)
