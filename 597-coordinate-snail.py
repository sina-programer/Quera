# https://quera.org/problemset/597

n = int(input())
d, m = divmod(n+2, 4)
x = y = d

if m == 0:
    y -= 1

if m in [2, 3]:
    x *= -1
if m in [3, 0]:
    y *= -1

print(x, y)
