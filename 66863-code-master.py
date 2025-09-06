# https://quera.org/problemset/66863

import math


def is_prime(x):
    if x == 2:
        return True
    elif (x < 2) or (x%2 == 0):
        return False

    for i in range(3, int(x**.5)+1, 2):
        if x % i == 0:
            return False

    return True


def get_primes():
    yield 2

    x = 3
    while True:
        if is_prime(x):
            yield x

        x += 2


def length(x, b=10):
    return math.floor(math.log(x, b)) + 1


def is_vip(x, base):
    ''' checks the symmetry of <x> in <base> radix at the same time '''
    n = length(x, base)
    for i in range(n//2):
        j = n - i - 1
        a = x % (base ** (i+1)) // (base ** i)
        b = x % (base ** (j+1)) // (base ** j)
        if a != b:
            return False
    return True


n, k = map(int, input().split())
primes = get_primes()

while True:
    prime = next(primes)
    d, m = divmod(length(prime, k), 2)
    if m == 0 and d > 1:
        continue

    if is_vip(prime, k):
        n -= 1
        if n == 0:
            print(prime)
            break
