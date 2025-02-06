# https://quera.org/problemset/20256

colors = input()
Y_count = colors.count('Y')
R_count = colors.count('R')
all_danger = False
for color in colors:
    if color not in ['Y', 'R']:
        break
else:
    all_danger = True

if R_count >= 3:
    print('nakhor lite')
elif R_count >= 2 and Y_count >= 2:
    print('nakhor lite')
elif all_danger:
    print('nakhor lite')
else:
    print('rahat baash')
