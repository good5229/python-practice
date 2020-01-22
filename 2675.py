import sys


def word_print():
    test_rep = sys.stdin.readline()
    for j in range(int(test_rep)):
        n, word = sys.stdin.readline().split()
        text = ''
        for i in range(len(word)):
            text += word[i] * int(n)
        print(text)


word_print()


