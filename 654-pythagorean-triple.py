# https://quera.org/problemset/654


def factorize(n):
    roots = []
    x = 2
    while n >= x:
        while n%x == 0:
            roots.append(x)
            n //= x
        x += 1
    return roots


def parse(n):
    if n%2:
        return

    for i in range(int(n/2)+1, 2, -1):
        m = n - i

        for j in range(int(m/2)+1, 2, -1):
            k = m - j

            a, b, c = sorted((i, j, k))
            if c**2 == a**2 + b**2:
                return a, b, c


def f(n):
    roots = factorize(n)

    m = 1
    for r in set(roots):
        roots.remove(r)
        m *= r

    while ((p := parse(m)) is None) and roots:
        m *= roots.pop(0)

    k = n // m
    if p is not None:
        return [x*k for x in p]


n = int(input())
result = f(n)

if result is not None:
    print(*result)
else:
    print('Impossible')
