soma_idade = 0
media_idade = 0
nome_homem_mais_velho = ''
idade_homem_mais_velho = 0
total_mulheres_menos_20 = 0

for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome da {}ª pessoa: '.format(c))).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    # Soma a idade de todo mundo
    soma_idade += idade
    
    # lógica de verificação do mais velho:
    if c == 1 and sexo == 'M':
        nome_homem_mais_velho = nome
        idade_homem_mais_velho = idade
    elif sexo == 'M' and idade > idade_homem_mais_velho: # Juntei seu else com if
        nome_homem_mais_velho = nome
        idade_homem_mais_velho = idade
        
    # lógica contar as mulheres:
    if sexo == 'F' and idade < 20:
        total_mulheres_menos_20 += 1

# Tirei os prints de dentro do for para eles só aparecerem no final de tudo
print('\n================ RESULTADOS ================')
media_idade = soma_idade / 4
print('A média de idade do grupo é de {} anos.'.format(media_idade))

if idade_homem_mais_velho == 0:
    print('Não temos nenhum homem neste grupo.')
else:
    print('O homem mais velho tem {} anos e se chama {}.'.format(idade_homem_mais_velho, nome_homem_mais_velho))

print('Ao todo são {} mulheres com menos de 20 anos.'.format(total_mulheres_menos_20))