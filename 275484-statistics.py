# https://quera.org/problemset/275484

c = 0
n = int(input())

p0 = int(input())
for _ in range(n-1):
    p = int(input())
    p0 = min(p0, p)
    c += max(0, p-p0)

print(c)
