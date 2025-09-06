# https://quera.org/problemset/221463

n, m = map(int, input().split())

for i in range(n):
    for j in range(m):
        p = '.'
        if i == 0 or j == 0:
            p = 'A'
        elif i == n-1 or j==m-1:
            p = 'B'
        print(p, end='')
    print()
