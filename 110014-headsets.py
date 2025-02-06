# https://quera.org/problemset/110014

h1 = input().split()
h2 = input().split()

if h1[0] == h1[1] or h2[0] == h2[1]:
	print('YES')
elif h1[0] == h2[1] or h2[0] == h1[1]:
	print('YES')
else:
	print('NO')
