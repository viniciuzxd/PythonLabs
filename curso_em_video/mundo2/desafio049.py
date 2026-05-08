n = int(input('Digite um número para ver sua tabuada: '))

print(f'Tabuada de {n}:')
for c in range(1, 11):
    print(f'{n} x {c} = {n * c}')