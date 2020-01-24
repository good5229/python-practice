import sys


def count_word():
    s = sys.stdin.readline().strip().upper()
    set_s = sorted(set(s))
    max = 0
    max_word = ''
    for i in set_s:
        if max < s.count(i):
            max = s.count(i)
            max_word = ""
            max_word += i
        elif max == s.count(i):
            max_word += i
    if len(max_word) > 1:
        return "?"
    else:
        return max_word


print(count_word())

