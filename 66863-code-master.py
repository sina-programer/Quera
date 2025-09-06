# https://quera.org/problemset/66863

import itertools as it
import string
import math

DIGITS = string.digits + string.ascii_uppercase


def is_prime(x):
    if x == 2:
        return True
    elif (x < 2) or (x%2 == 0):
        return False

    for i in range(3, int(x**.5)+1, 2):
        if x % i == 0:
            return False

    return True


def length(x, b=10):
    return math.floor(math.log(x, b)) + 1


def get_symmetrical_numbers(base=10):
    digits = DIGITS[:base]
    n = 1

    while True:
        d, m = divmod(n+1, 2)
        for comb in it.product(*([digits] * d)):
            if comb[0] == '0':
                continue
            yield int(''.join(comb + comb[:d+m-1][::-1]), base=base)

        n += 1


n, k = map(int, input().split())

for x in get_symmetrical_numbers(base=k):
    d, m = divmod(length(x, k), 2)
    if m == 0 and d > 1:
        continue

    if is_prime(x):
        n -= 1
        if n == 0:
            print(x)
            break
