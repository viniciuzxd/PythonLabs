from random import randint

print('-=' * 15)
print(' VAMOS JOGAR PAR OU ÍMPAR ? ')
print('-=' * 15)

vitorias = 0

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Você quer Par ou Ímpar? [P/I]: ')).strip().upper()[0]

    print('-' * 30)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    print('-' * 30)

    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitorias += 1
        else:
            print('Você PERDEU!')
            break # Game Over
            
    elif tipo == 'I':
        if total % 2 != 0:
            print('Você VENCEU!')
            vitorias += 1
        else:
            print('Você PERDEU!')
            break 
            
    print('Vamos jogar novamente...')
    print('-=' * 15)

print(f'GAME OVER! Você conquistou uma sequência de {vitorias} vitória(s).')