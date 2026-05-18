jogador = {}
partidas = []

jogador['nome'] = str(input('Nome do Jogador: ')).strip()
total_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range(0, total_partidas):
    gols = int(input(f'   Quantos gols na partida {c + 1}? '))
    partidas.append(gols)

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('-=' * 30)
print(jogador)
print('-=' * 30)

for chave, valor in jugador.items():
    print(f'O campo {chave} tem o valor {valor}')

print('-=' * 30)

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for indice, gols_partida in enumerate(jogador['gols']):
    print(f'    => Na partida {indice + 1}, fez {gols_partida} gols.')
print(f'Foi um total de {jogador["total"]} gols.')