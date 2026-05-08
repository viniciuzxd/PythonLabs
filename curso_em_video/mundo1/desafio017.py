from math import hypot

co = float(input('Comprimento do cateto oposto: ').replace(',', '.'))
ca = float(input('Comprimento do cateto adjacente: ').replace(',', '.'))

hi = (co ** 2 + ca ** 2) ** (1/2)
#or with the math library
hi = hypot(co, ca)

print('A hipotenusa vai medir {:.2f}.'.format(hi))

