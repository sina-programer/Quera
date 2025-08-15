# https://quera.org/problemset/272644

# solve as numbers in binary

n, q = map(int, input().split())
s = input()

for _ in range(q):
    flag, x = input().split()

    if flag == '?':
        print('YES' if x in s else 'NO')

    else:
        x = int(x) - 1
        new_char = str(abs(int(s[x]) - 1))
        s = s[:x] + new_char + s[x+1:]
