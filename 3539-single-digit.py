# https://quera.org/problemset/3539

x = input()
while len(x) > 1:
    x = str(sum(map(int, x)))
print(x)
