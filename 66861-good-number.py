# https://quera.org/problemset/66861

def tri_numbers():
    number = 1
    d = 2

    while True:
        yield number
        number += d
        d += 1


k = int(input())

for num in tri_numbers():
    counter = 0
    for i in range(1, num+1):
        if not num%i:
            counter += 1

    if counter >= k:
        print(num)
        break
