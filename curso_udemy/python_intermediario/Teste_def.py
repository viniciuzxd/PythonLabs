def soma (a, b, c=None):
    if c is not None:
        print(f'{a=} {b=} {c=}', a + b + c)
    else:
        print(f'{a=} {b=}', a + b)

soma (1, 2)
soma (3, 5)
soma(200, 500)
soma(100, 200, 0)
soma(b=6, a=4, c=7)