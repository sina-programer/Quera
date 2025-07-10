# https://quera.org/problemset/2659

n = int(input())
p1 = input()
p2 = input()

print(
    sum(
        1 if p1[i] != p2[i] else 0
        for i in range(n)
    )
)
