# https://quera.org/problemset/3539

x = int(input())

while x > 9:
    s = 0

    while x > 0:
        d, m = divmod(x, 10)
        s += m
        x = d

    x = s

print(x)
