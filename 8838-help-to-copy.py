# https://quera.org/problemset/8838

n, string = input().split()

repeats = ['copy of' for _ in range(int(n))]
repeats.append(string)

result = ' '.join(repeats)
print(result)
