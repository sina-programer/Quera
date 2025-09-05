# https://quera.org/problemset/76278

def calculator(n, m, array):
    value = 0
    i = 0
    ceil = n // m
    while i <= ceil:
        value += sum(array[i*m : (i+1)*m]) * (-1) ** (i%2)
        i += 1

    return value
