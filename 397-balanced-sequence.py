# https://quera.org/problemset/397

clause = input()
changes = 0
opens = 0

for char in clause:
    if char == '(':
        opens += 1
    else:
        opens -= 1

    if opens < 0:
        changes += 1
        opens += 2

changes += opens // 2
print(changes)
