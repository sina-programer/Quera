# https://quera.org/problemset/9722


def is_prime(n):
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, n//2+1):
        if n % i == 0:
            return False

    return True


def is_hard(n: str):
    length = len(n)
    for i in range(length):
        if not is_prime(int(n[:i+1])):
            return False
    return True


N = int(input())
digits = list('1379')
primes = list(map(str, filter(is_prime, range(10))))

for _ in range(2, N+1):
    new_primes = []
    for prime in primes:
        for digit in digits:
            new_number = prime + digit
            if is_hard(new_number):
                new_primes.append(new_number)
    primes = new_primes

print('\n'.join(sorted(primes)))
