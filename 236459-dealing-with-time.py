# https://quera.org/problemset/236459

import math

k = int(input())
n = int(input())
buildings = list(map(int, input().split())) + [0]
c = 0
t = -1

for b in buildings:
    l = math.fabs(b - c)
    c = b
    t += math.ceil(l / k) + 1

print(t)
