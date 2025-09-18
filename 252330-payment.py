# https://quera.org/problemset/252330

import string

chars = string.ascii_lowercase

t = int(input())
for _ in range(t):
    counts = {c: 0 for c in chars}

    n = int(input())
    for _ in range(n):

        word = input()
        for char in chars:
            counts[char] = max(counts[char], word.count(char))

    ans = sum(map(counts.get, counts))
    print(ans)
