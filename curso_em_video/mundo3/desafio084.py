pessoas = []
dado_temp = []
maior_peso = menor_peso = 0

while True:
    dado_temp.append(str(input('Nome: ')))
    dado_temp.append(float(input('Peso: ')))
    
    if len(pessoas) == 0:
        maior_peso = menor_peso = dado_temp[1]
    else:
        if dado_temp[1] > maior_peso:
            maior_peso = dado_temp[1]
        if dado_temp[1] < menor_peso:
            menor_peso = dado_temp[1]
            
    pessoas.append(dado_temp[:]) 
    dado_temp.clear()
    
    resp = input('Quer continuar? [S/N] ').upper().strip()[0]
    while resp not in 'SN':
        resp = input('Opção inválida. Quer continuar? [S/N] ').upper().strip()[0]
    if resp == 'N':
        break

print('-=' * 30)

# A) Quantidade
print(f'A) Ao todo, você cadastrou {len(pessoas)} pessoas.')

# B) Pessoas mais pesadas
print(f'B) O maior peso foi de {maior_peso}Kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == maior_peso:
        print(f'[{p[0]}] ', end='')
print()

print(f'C) O menor peso foi de {menor_peso}Kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == menor_peso:
        print(f'[{p[0]}] ', end='')
print()