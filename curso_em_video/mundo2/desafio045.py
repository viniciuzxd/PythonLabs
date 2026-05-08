from random import choice

print('-=' * 4)
print('JOKENPÔ')
print('-=' * 4)

opcoes = ['PEDRA', 'PAPEL', 'TESOURA']

jogador = input('Escolha PEDRA, PAPEL ou TESOURA: ').upper()

computador = choice(opcoes)

if jogador == computador:
    print('EMPATE!')
elif (jogador == 'PEDRA' and computador == 'TESOURA') or (jogador == 'PAPEL' and computador == 'PEDRA') or (jogador == 'TESOURA' and computador == 'PAPEL'):
    print('VOCÊ VENCEU!')
else:
    print('COMPUTADOR VENCEU!')