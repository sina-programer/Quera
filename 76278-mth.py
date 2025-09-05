# https://quera.org/problemset/76278

def windowise(array, w):
    i = 0
    while True:
        sub = array[i*w : (i+1)*w]
        if sub:
            yield sub
        else:
            break
        i += 1

def calculator(n, m, array):
    return sum(
        [
            sum(window) * ((-1) ** i)
            for i, window in enumerate(windowise(array, m))
        ]
    )
