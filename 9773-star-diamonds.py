# https://quera.org/problemset/9773

k = 2  # number of diamonds
n = int(input())
m = int(n / 2) + 1

for i in range(1, n+1):
    d = abs(m - i)
    dd = (m - d) * 2 - 1

    for _ in range(k):
        print(' ' * d, end='')
        print('*' * dd, end='')
        print(' ' * d, end='')
    print()
