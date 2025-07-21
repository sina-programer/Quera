# https://quera.org/problemset/221462

n = 3
P = [list(map(int, input().split())) for _ in range(2**n - 1)]
assert all(map(lambda row: len(row) == n, P))
P = [[P[k][i] for k in range(len(P))] for i in range(n)]  # transpose

print(*(min(P[i], key=P[i].count) for i in range(n)))
