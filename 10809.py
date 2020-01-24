import sys


def count():
    n = sys.stdin.readline().strip()

    alphabets = "abcdefghijklmnopqrstuvwxyz"
    text = ''
    for alphabet in alphabets:
        text += str(n.find(str(alphabet)))+" "

    print(text)


count()

