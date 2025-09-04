# https://quera.org/problemset/254220

def compare(key, guess):
    n = len(key)
    m = len(guess)

    if n != m:
        return 'Invalid Length'

    result = [''] * n
    for i in range(n):
        if key[i] == guess[i]:
            result[i] = 'G'

    idxes = [i for i in range(n) if result[i]=='']

    for i in idxes.copy():
        char = guess[i]
        status = 'R'

        for jj, j in enumerate(idxes):
            if char == key[j]:
                status = 'Y'
                idxes.pop(jj)
                break

        result[i] = status

    return ''.join(result)


key = list(input())
n = int(input())

found = False
for i in range(n):
    if found:
        print('Game Over')
        continue

    guess = input()
    state = compare(key, guess)
    print(state)

    if state.count('G') == len(state):
        found = True
