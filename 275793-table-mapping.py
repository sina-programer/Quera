# https://quera.org/problemset/275793

import math

def get_number_of_lines(x):
    return math.floor((x-1)/2)

def is_neighbor(i, j):
    if abs(i - j) == 1:
        return True

def show_table():
    for row in table:
        print(''.join(row))


n, m, k = list(map(int, input().split()))

n_lines = get_number_of_lines(n)
m_lines = get_number_of_lines(m)
k_lines = k - 1

n_areas = n_lines + 1
m_areas = m_lines + 1

k_max = n_areas * m_areas

if (n%2 or m%2) and (n_lines > 0) and (m_lines > 0):
    k_max -= 1

if k > k_max:
    print(-1)

else:
    table = [['O' for j in range(m)] for i in range(n)]

    i = 1
    while (i < n-1) and (k_lines > 0):
        table[i] = ['X' for _ in range(m)]
        k_lines -= 1
        i += 2


    j = 1
    while (j < m-1) and (k_lines > 0):
        j_old = j

        d = 1
        i = 0
        while (i < n) and (k_lines > 0):
            table[i][j] = 'X'
            if i == n-2:
                table[n-1][j] = 'X'
            k_lines -= 1
            i += 2
            j += d
            d *= -1

        j = j_old
        j += 2


    show_table()
