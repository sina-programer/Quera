# https://quera.org/problemset/255962

def evaluate(code):
    c = 0
    for i, x in enumerate(code[-2::-1], start=2):
        c += i * int(x)
    return c % 11


t = int(input())

for _ in range(t):
    clause = input()
    answer = None
    count = 0

    for x in range(10):
        code = clause.replace('?', str(x))
        s10 = int(code[-1])
        c = evaluate(code)
        if (c in [0, 1] and s10 == c) or (s10 == 11-c):
            answer = code
            count += 1

    if count == 1:
        print(answer)
    elif count == 0:
        print('cannot be recovered!')
    else:
        print("it's not unique!")
