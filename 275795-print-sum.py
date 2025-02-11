# https://quera.org/problemset/275795

n = int(input())
nums = range(1, n+1)
summation = sum(nums)
print(' + '.join(map(str, nums)), '=', summation)
