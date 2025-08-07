# https://quera.org/problemset/232025

t = int(input())
for _ in range(t):
    n = int(input())
    scores = input()
    if scores.count('Q') > n/2:
        print('Quera')
    else:
        print('CodeCup')
