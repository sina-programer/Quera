# https://quera.org/problemset/282

n = int(input())
s = 0

for x in range(1, n//2+1):
    if n % x == 0:
        s += x

if n == s:
    print('YES')
else:
    print('NO')
