# https://quera.org/problemset/66864

k = int(input())

b = 0  # foregoing boundary
n = 0  # number of digits
while True:
    boundary = b + int(n * 9 * (10 ** (n-1)))
    if k <= boundary:
        break
    b = boundary
    n += 1

# d: index of desired number between all n-digits
# m: index of digit in the number
d, m = divmod(k-b-1, n)
x = (10 ** (n-1)) + d  # target number
for _ in range(n-m):
    xx, digit = divmod(x, 10)
    x = xx
print(digit)
