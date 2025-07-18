# https://quera.org/problemset/140033

vowels = tuple('aeiou')
word = input().lower()
count = sum(map(word.count, vowels))
print(count)
