# https://quera.org/problemset/221462

X, Y, Z = [], [], []

for _ in range(7):
    x, y, z = map(int, input().split())
    X.append(x)
    Y.append(y)
    Z.append(z)

print(
    min(set(X), key=X.count),
    min(set(Y), key=Y.count),
    min(set(Z), key=Z.count)
)
