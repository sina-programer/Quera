# https://quera.org/problemset/9774

n = input()

for i in n:
    print(f'{i}: ', end='')
    for j in range(int(i)):
        print(i, end='')

    print()
