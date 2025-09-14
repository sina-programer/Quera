# https://quera.org/problemset/26110

bins = list(range(10, 200, 20))

n = int(input())
score = 0

for i in range(n):
    x, y = map(float, input().split())
    d = (x**2 + y**2) ** .5

    for b in bins:
        if d <= b:
            score += 1

print(score)
