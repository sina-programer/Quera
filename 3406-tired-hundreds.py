# https://quera.org/problemset/3406

a = input()
b = input()

res_a = 0
res_b = 0

for p, (i, j) in enumerate(zip(a, b)):
    res_a += (10 ** p) * int(i)
    res_b += (10 ** p) * int(j)


if res_a == res_b:
    print(f"{a} = {b}")
    
elif res_a < res_b:
    print(f"{a} < {b}")
    
elif res_b < res_a:
    print(f"{b} < {a}")
