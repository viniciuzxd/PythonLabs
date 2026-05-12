list_temp = []

for c in range(1, 5):
    num = int(input('Digite um número: '))
    list_temp.append(num)

numeros = tuple(list_temp)

print('Os números digitados foram: {}'.format(numeros), end='')
print('\nO valor 9 apareceu {} vezes.'.format(numeros.count(9)))
print('O primeiro valor 3 foi digitado na posição {}.'.format(numeros.index(3) + 1))

for n in numeros:
    if n % 2 == 0:
        print('Os números pares digitados foram: {}'.format(n), end=' ')