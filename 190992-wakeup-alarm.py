# https://quera.org/problemset/190992

h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

s = s2 - s1
if s < 0:
    s += 60
    m2 -= 1

m = m2 - m1
if m < 0:
    m += 60
    h2 -= 1

h = h2 - h1
if h < 0:
    h += 24

if s == m == h == 0:
    h = 24

delta = f"{h:02}:{m:02}:{s:02}"
print(delta)
