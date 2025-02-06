# https://quera.org/problemset/2529

n = int(input())
lens = []

for i in range(n):
    lens.append(len(set(input())))

print(max(lens))
