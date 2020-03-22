entire = set(i for i in range(1, 10001))

# n = 1
# while n <= 10000:
#     num_len = len(str(n))
#     sum_len = 0
#     for i in range(num_len):
#         sum_len += int(str(n)[i])
#     remove_num = n + sum_len
#     if remove_num in entire:
#         entire.remove(remove_num)
#     n += 1
#
# for num in entire:
#     print(num)
