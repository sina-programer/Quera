# https://quera.org/problemset/3405

n = int(input())
numbers = []

while n:
    numbers.append(n)
    n = int(input())

for n in reversed(numbers):
    print(n)
