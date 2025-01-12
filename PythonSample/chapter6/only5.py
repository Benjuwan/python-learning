def f(a, /, b, *c, d, **e):
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('d:', d)
    print('e:', e)

f(1, 2, d=5)
