# https://quera.org/problemset/111990

days = {
    'shanbe': 0,
    'yekshanbe': 1,
    'doshanbe': 2,
    'seshanbe': 3,
    'chaharshanbe': 4,
    'panjshanbe': 5,
    'jome': 6
}

day = days.get(input())

if day == 6:
    print('tatil')
elif day%2:
    print('bahman')
else:
    print('perspolis')
