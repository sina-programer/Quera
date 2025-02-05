# https://quera.org/problemset/148099

n = int(input())
numbers = list(map(int, input().split()))
unique_nums = []
for n in numbers:
    if numbers.count(n) == 1:
        unique_nums.append(n)

res = 0
for n in unique_nums:
    res ^= n

print(res)
