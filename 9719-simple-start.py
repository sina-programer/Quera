# https://quera.org/problemset/9719

dec_to_str = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A',
              11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K'}


def decimal_to(number: int, base):
    divisions = []
    out = number // base
    over = number % base
    divisions.append(dec_to_str.get(over))

    while out >= base:
        out, over = out // base, out % base
        divisions.append(dec_to_str.get(over))

    else:
        divisions.append(dec_to_str.get(out))

    divisions.reverse()
    H = ''.join(divisions)

    return H.lstrip('0')


b = int(input())
number = 1

while number < 300:
    number_b = decimal_to(number, b)
    square_b = decimal_to(number**2, b)
    if square_b == square_b[::-1]:
        print(number_b, square_b)

    number += 1
