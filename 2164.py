import sys
import collections

# n = int(sys.stdin.readline().strip())
# card_list = [_ for _ in range(n, 0, -1)]
# card_len = len(card_list)
# if n == 1:
#     print("1")
# while card_len >= 2:
#     del card_list[-1]
#     card_len -= 1
#     card_list.insert(0, card_list[-1])
#     del card_list[-1]
#
# print(card_list[0])

card_num = int(sys.stdin.readline().strip())
card_deque = collections.deque([i for i in range(1, card_num+1)])

while len(card_deque) != 1:
    card_deque.popleft()
    card_deque.rotate(-1)

print(card_deque[0])
