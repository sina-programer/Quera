# https://quera.org/problemset/33473

import math

def square(x): return x ** 2

def circle(r): return math.pi * r ** 2

def rectangle(a, b): return a * b

def triangle(a, b): return a * b / 2

def get_func(ls):
    return list(map(eval, ls))
