import sys

ans = ""
while True:
    n = sys.stdin.readline().strip()
    if n == "0":
        break
    else:
        if len(n) % 2 == 1:
            mid = int(len(n) / 2)
            word_left = n[:mid]
            word_right = n[mid + 1:]
            if word_left == word_right[::-1]:
                ans += "yes\n"
            else:
                ans += "no\n"
        else:
            mid = int(len(n) / 2)
            word_left = n[:mid]
            word_right = n[mid:]
            if word_left == word_right[::-1]:
                ans += "yes\n"
            else:
                ans += "no\n"
print(ans)

