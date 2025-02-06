# https://quera.org/problemset/91712

x1, x2 = list(map(int, input().split()))
direction = 'L' if x1 - x2 > 0 else 'R'
diff = abs(x1 - x2)

if x1 == x2:
    print('Saal Noo Mobarak!')
else:
    print(diff * direction)
