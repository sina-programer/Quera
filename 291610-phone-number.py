# https://quera.org/problemset/291610

n = int(input())

for _ in range(n):
    phone = input()
    if phone.startswith('09'):
        phone = '98' + phone[1:]
    elif phone.startswith('+98'):
        phone = phone[1:]

    if phone.startswith('98') and phone.isdigit() and len(phone)==12:
        print('+' + phone)
    else:
        print('invalid')
