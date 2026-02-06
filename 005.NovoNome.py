# Interação de strings com while
nome = 'Gabriel Vinicius'

# Detalhes Nome
tamanho = len(nome)

indice = 0
novo = ''
while indice < tamanho:
    letra = nome[indice]
    novo += f'/{letra}'
    indice += 1

print(novo)
