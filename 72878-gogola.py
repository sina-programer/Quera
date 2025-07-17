# https://quera.org/problemset/72878

t, a, b = list(map(int, input().split()))
ar = ma = 0

d, m = divmod(t, a+b+2)
ar += d
ma += d

sign = min(1, m)
ar += sign
m -= sign

if m >= a+1:
    m -= a+1
    ma += 1

print(ar, ma)
