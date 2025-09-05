# https://quera.org/problemset/87176

def game(x):
    a, b = divmod(x, 10)
    if b > a:
        a, b = b, a
    return a - b
