v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
v3 = int(input('Digite mais um valor: '))

menor = v1
if v2 < menor:
    menor = v2
if v3 < menor:
    menor = v3

maior = v1
if v2 > maior:
    maior = v2
if v3 > maior:
    maior = v3

print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))

#or

print('O menor valor é {}'.format(menor = min(v1, v2, v3)))
print('O maior valor é {}'.format(maior = max(v1, v2, v3)))