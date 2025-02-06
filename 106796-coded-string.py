# https://quera.org/problemset/106796

import string

letters = list(string.ascii_lowercase * 2)

length = int(input())
times = int(input())
phrase = input()

for time in range(times):
    phrase = phrase[-1] + phrase[:-1]
    temp = list(phrase)
    for idx, char in enumerate(temp):
        temp[idx] = letters[letters.index(char) + 1]

    phrase = ''.join(temp)

print(phrase)
