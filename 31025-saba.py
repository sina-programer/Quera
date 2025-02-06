# https://quera.org/problemset/31025

import math

n, k = list(map(int, input().split()))

for i in range(k):
    n /= 2

print(math.floor(n))
