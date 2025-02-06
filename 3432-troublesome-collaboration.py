# https://quera.org/problemset/3432

# n --> Mohammad Javad
# m --> Mostafa

n, m = list(map(int, input().split()))
works_n = set(input().split())
works_m = set(input().split())

if works_n == works_m:
    print('Both')
elif works_n.issuperset(works_m):
    print('Mostafa')
elif works_m.issuperset(works_n):
    print('Mohammad Javad')
else:
    print('None')
