import sys

def check_croatian(text):
    croatia_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

    for i in croatia_alphabet:
        text = text.replace(i, '*')
    return len(text)


word = sys.stdin.readline().strip()
print(check_croatian(word))
