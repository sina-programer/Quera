# https://quera.org/problemset/102248

def compare(s1, s2):
    while s1 and s2:
        o1 = ord(s1[0])
        o2 = ord(s2[0])
        if o1 <= o2:
            s1 = s1[1:]
        if o2 <= o1:
            s2 = s2[1:]

        if s2:
            s1 = s1[::-1]
        if s1:
            s2 = s2[::-1]

    return s1 or s2 or 'Both strings are empty!'
