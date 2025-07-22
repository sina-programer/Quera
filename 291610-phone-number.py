# https://quera.org/problemset/291610

n = int(input())

for _ in range(n):
    phone = input()

    if phone.startswith('09') and phone.isdigit() and len(phone)==11:
        print('+98' + phone[1:])
    elif phone.startswith('98') and phone.isdigit() and len(phone)==12:
        print('+' + phone)
    elif phone.startswith('+98') and phone[1:].isdigit() and len(phone)==13:
        print(phone)
    else:
        print('invalid')
