import sys

n = int(sys.stdin.readline().strip())
score_list = [0]

for i in range(n):
    score_list.append(int(sys.stdin.readline().strip()))


sum_of_score = [0]
sum_of_score.append(score_list[1])
sum_of_score.append(score_list[1] + score_list[2])
sum_of_score.append(max(score_list[3] + score_list[1], score_list[3] + score_list[2]))

for i in range(4, n + 1):
    sum_of_score.append(
        max(score_list[i] + sum_of_score[i - 2], score_list[i] + score_list[i - 1] + sum_of_score[i - 3]))

print(sum_of_score[-1])
