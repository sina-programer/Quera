# https://quera.org/problemset/275517

import itertools as it

def algorithm(array):
    array = list(array)
    length = len(array)
    for i in range(length-1, 0, -1):
        j = i // 2
        if array[i] < array[j]:
            array[i], array[j] = array[j], array[i]
    return array


t = int(input())

for i in range(t):
    n = int(input())

	# shortcut method
	# print(2 ** (n-1))

    # main method
    c = 0
    numbers = list(range(1, n+1))
    for perm in it.permutations(numbers):
        if algorithm(perm) == numbers:
            c += 1
    print(c)
