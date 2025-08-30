# https://quera.org/problemset/2530

word = input()

c = (
    word.count('T')
    + word.count('D')
    + word.count('L')
    + word.count('F')
)

print(2 ** c)
