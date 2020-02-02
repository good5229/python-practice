import sys

n = int(sys.stdin.readline().strip())
inventory = []
text = ""
for i in range(n):
    p, w = map(int, sys.stdin.readline().strip().split())
    inventory.append([p, w])

    z = sorted(inventory, key=lambda x: (-x[0] / x[1]))
    power = 0
    weight = 0
    if len(z) >= 8:
        for i in range(8):
            power += z[i][0]
            weight += z[i][1]
        text += f'{power/weight}'
print(text)
