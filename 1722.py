import itertools
import sys

n = int(sys.stdin.readline().strip())
second = sys.stdin.readline().strip()
state = [i for i in range(1, n + 1)]
cnt = 1
if second[0] == "1":
    second_key = int(second[1:].strip())
    for s in itertools.permutations(state, n):
        s = list(s)
        if cnt == second_key:
            for j in s:
                print(j, end=' ')
            break
        else:
            cnt += 1
elif second[0] == "2":
    second_key = list(map(int, second[1:].split()))
    for s in itertools.permutations(state, n):
        s = list(s)
        if second_key == s:
            print(cnt)
        else:
            cnt += 1
