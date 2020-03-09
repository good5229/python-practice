import itertools
import sys

N = int(sys.stdin.readline().strip())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
members = [i for i in range(N)]
possible_team = []

for team in list(itertools.combinations(members, N // 2)):
    possible_team.append(team)

min_stat_gap = 10000
for i in range(len(possible_team) // 2):
    team = possible_team[i]
    stat_A = 0
    for j in range(N // 2):
        member = team[j]
        for k in team:
            stat_A += S[member][k]

    team = possible_team[-i - 1]
    stat_B = 0
    for j in range(N // 2):
        member = team[j]
        for k in team:
            stat_B += S[member][k]

    min_stat_gap = min(min_stat_gap, abs(stat_A - stat_B))

print(min_stat_gap)
