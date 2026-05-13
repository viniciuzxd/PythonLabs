valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    
    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break

print('-=' * 30)
print(f'Você digitou {len(valores)} números.')
print(f'Os valores em ordem decrescente são: {sorted(valores, reverse=True)}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')  