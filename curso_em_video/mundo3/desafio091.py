from random import randint
from time import sleep
from operator import itemgetter

jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}

ranking = list()

print('Valores sorteados:')
for chave, valor in jogo.items():
    print(f'{chave} tirou {valor} no dado.')
    sleep(1)

print('-=' * 20)
print('  == RANKING DOS JOGADORES ==')

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=reverse=True)

for indice, valor in enumerate(ranking):
    print(f'   {indice+1}º lugar: {valor[0]} com {valor[1]}.')
    sleep(1)