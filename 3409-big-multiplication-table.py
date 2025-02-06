# https://quera.org/problemset/3409

n = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        print(format(i*j, f'<{len(str(n*n))+1}'), end='')

    print()
