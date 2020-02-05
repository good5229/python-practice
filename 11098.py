import sys

n = int(sys.stdin.readline().strip())

for i in range(n):
    m = int(sys.stdin.readline().strip())
    players = []
    for j in range(m):
        value, name = sys.stdin.readline().split()
        players.append((int(value), name))

    players.sort(key=lambda x: (x[0], x[1]), reverse=True)
    print(players[0][1])