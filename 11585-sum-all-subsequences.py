# https://quera.org/problemset/11585

n = int(input())
A = map(int, input().split())

s = 0
for i, a in enumerate(A, start=1):
    s += a * i * (n-i+1)

print(s)
