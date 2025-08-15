# https://quera.org/problemset/293

a = int(input())
b = int(input())

while a <= b:

    c = 0
    for x in range(1, a//2+1):
        c += abs(min(a % x - 1, 0))

    if c == 1:
        print(a)

    a += 1
