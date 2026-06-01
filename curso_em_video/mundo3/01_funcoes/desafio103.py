n = str(input('Nome do jogador: ')).strip()
g = str(input('Número de gols: ')).strip()

def ficha(nome='<desconecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

if n == '':
    n = '<desconecido>'
if g == '':
    g = 0
ficha(n, g)

print('---' * 10)
# Outra forma de fazer, usando a função ficha() para validar os dados:
def ficha(nome='<desconecido>', gols=0):
    if nome.strip() == '':
        nome = '<desconecido>'
    if gols.strip() == '':
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

ficha(n, g)