# https://quera.org/problemset/108665

n = input()
vowels = tuple('aeiou')
counter = 0

for vowel in vowels:
    counter += n.count(vowel)

print(2 ** counter)
