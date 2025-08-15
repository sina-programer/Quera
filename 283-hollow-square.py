# https://quera.org/problemset/283

a = int(input())
b = int(input())
d = a - b
dd = d // 2
m = (a-1) / 2

if d <= 0:
    print('Wrong order!')

elif d%2:
    print('Wrong difference!')

else:
    for i in range(a):
        # if (i < dd) or (i >= a-dd):
        if abs(m-i) > m-dd:
            print('* ' * a)
        else:
            print(
                '* ' * dd,
                '  ' * b,
                '* ' * dd,
                sep=''
            )
