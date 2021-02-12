def my_f(word):
    return word[0].title() + word[1:].lower()
s = input().split()
for i, word in enumerate(s):
    if not word.isascii() or not word.isalpha() or not word.islower():
        print('error!')
    else:
        s[i] = my_f(word)
print(' '.join(s))