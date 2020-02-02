import sys

n = int(sys.stdin.readline().strip())
for i in range(n):
    basic_hp, basic_mp, attack, defense, add_hp, add_mp, add_att, add_def = map(int, sys.stdin.readline().split())
    calc_hp = basic_hp + add_hp
    calc_mp = basic_mp + add_mp
    calc_att = attack + add_att
    if calc_hp < 1:
        calc_hp = 1
    if calc_mp < 1:
        calc_mp = 1
    if calc_att < 0:
        calc_att = 0
    power = 1 * calc_hp + 5 * calc_mp + 2 * calc_att + 2 * (defense + add_def)
    print(power)
