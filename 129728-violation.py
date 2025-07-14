# https://quera.org/problemset/129728

print(' '.join(sorted([chr(ord(char) + 32*(ord(char)%2-1)) for char in input()], reverse=True)))
