# https://quera.org/problemset/305

def gcd(x, y):
    if y > x:
        x, y = y, x

    d, m = divmod(x, y)
    if m == 0:
        return y
    return gcd(y, m)


a = int(input())
b = int(input())

print(gcd(a, b))
