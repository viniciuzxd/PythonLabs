n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print(f'O número {n1} é maior que o número {n2}.')
elif n2 > n1:
    print('O número {} é maior que o número {}.'.format(n2, n1))
else:
    print('Os números são iguais.')

#or

if n1 > n2:
    print('O primeiro valor é maior!')
elif n2 > n1:
    print('O segundo valor é maior!')
else:
    print('Os valores são iguais!')