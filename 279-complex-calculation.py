# https://quera.org/problemset/279

from math import comb

a, x, n = map(int, input().split())
# (a + x) ** n
s = sum(comb(n, k) * a**k * x**(n-k) for k in range(n+1))
print(s)
