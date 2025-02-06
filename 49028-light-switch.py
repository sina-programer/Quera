# https://quera.org/problemset/49028

n = int(input())
modes = []
counter = 0

for i in range(n):
    modes.append(input())

for i in range(len(modes)-1):
    if modes[i] != modes[i+1]:
        counter += 1

print(counter)
