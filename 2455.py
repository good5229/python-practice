import sys

train_list = []
for i in range(4):
    n, k = map(int, sys.stdin.readline().split())
    train_list.append((n, k))

max_population = 0
population = 0
for i in range(len(train_list)):
    population += train_list[i][1]
    population -= train_list[i][0]
    if max_population < population:
        max_population = population


print(max_population)
