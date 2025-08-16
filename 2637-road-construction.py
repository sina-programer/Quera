# https://quera.org/problemset/2637

from math import floor, ceil

n = int(input())

a = floor(n / 2) + 1
b = ceil(n / 2) + 1

c = a * b
print(c)
