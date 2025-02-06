# https://quera.org/problemset/2659

n = int(input())
base = input()
user = input()
letters = []

for idx, letter in enumerate(user):
    if base[idx] != letter:
        letters.append(letter)

print(len(letters))
