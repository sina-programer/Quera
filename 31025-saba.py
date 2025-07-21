# https://quera.org/problemset/31025

import math

n, k = list(map(int, input().split()))
n /= (2 ** k)
print(math.floor(n))
