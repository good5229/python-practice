import sys

l = 0
while True:
    try:
        for word in sys.stdin.readline().split():
            if word == '<br>':
                l = 0
                print('')
            elif word == '<hr>':
                if l:
                    print('\n' + '-' * 80)
                else:
                    print('-' * 80)
                    l = 0
            else:
                word_len = len(word)
                if l + word_len > 80:
                    l = word_len
                    print()
                    print(word, end='')
                else:
                    l += word_len
                    print(word, end='')
                if l + 1 > 80:
                    l = 0
                    print()
                else:
                    l += 1
                    print(' ', end='')
    except:
        break
