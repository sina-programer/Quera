# https://quera.org/problemset/129726

def separator(ls):
    odds = []
    evens = []

    for item in ls:
        if item % 2:
            odds.append(item)
        else:
            evens.append(item)

    return evens, odds
