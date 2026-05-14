pares = []
impares = []

while True:
    for n in range(1, 8):
        valor = int(input(f'Digite o {n}º valor: '))
        if valor % 2 == 0:
            pares.append(valor)
        else:
            impares.append(valor)
    
    resp = input('Quer continuar? [S/N] ').upper().strip()[0]
    while resp not in 'SN':
        resp = input('Opção inválida. Quer continuar? [S/N] ').upper().strip()[0]
    if resp == 'N':
        break

print('-=' * 30)
print(f'Os valores pares digitados foram: {sorted(pares)}')
print(f'Os valores ímpares digitados foram: {sorted(impares)}')
print('-=' * 30)