import sys


def word_count():
    word = sys.stdin.readline().strip()
    print(len(word.split()))


word_count()
