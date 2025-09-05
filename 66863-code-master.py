# https://quera.org/problemset/66863

import string

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


def get_primes():
    yield 2

    x = 3
    while True:
        if is_prime(x):
            yield x

        x += 2


def to_base(x: int, base: int) -> str:
    digits = []
    while x:
        d, m = divmod(x, base)
        digits.insert(0, DIGITS[m])
        x = d

    return ''.join(digits)


def is_symmetric(clause: str):
    n = len(clause)
    for i in range(n//2+1):
        j = n - i - 1
        if clause[i] != clause[j]:
            return False
    return True



n, k = map(int, input().split())
primes = get_primes()

while True:
    prime = next(primes)

    if is_symmetric(to_base(prime, k)):
        n -= 1
        if n == 0:
            print(prime)
            break
