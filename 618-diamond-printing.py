# https://quera.org/problemset/618

n = int(input())

for i in range(2*n+1):
    d = abs(n-i)
    print(' ' * d, end='')
    print('*' * (abs(n-d+1)*2-1))
