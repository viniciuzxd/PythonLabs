galera = list()
pessoa = dict()

soma_idade = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip()
    
    # Validação do sexo
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
        
    pessoa['idade'] = int(input('Idade: '))
    soma_idade += pessoa['idade']
    
    galera.append(pessoa.copy())
    
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
        
    if resposta == 'N':
        break

print('-=' * 30)

total_pessoas = len(galera)
print(f'A) Ao todo, temos {total_pessoas} pessoas cadastradas.')

media_idade = soma_idade / total_pessoas
print(f'B) A média de idade é de {media_idade:.2f} anos.')

print('C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'[{p["nome"]}] ', end='')
print()

print('D) Lista das pessoas que estão acima da média:')
for p in galera:
    if p['idade'] >= media_idade:
        print('    ', end='')
        for chave, valor in p.items():
            print(f'{chave} = {valor}; ', end='')
        print()
        
print('<<< ENCERRADO >>>')