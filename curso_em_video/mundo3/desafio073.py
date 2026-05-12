times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional',
         'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco',
         'Vitória', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude',
         'Bragantino', 'Athletico-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá')

while True:
    print('-' * 30)
    opc = int(input('''Digite a opção desejada:
[1] - Times em ordem alfabética
[2] - Posição de um time específico
[3] - Os 5 primeiros colocados
[4] - Os 4 últimos colocados
[5] - Sair do programa
>>> '''))
    print('-' * 30)

    if opc == 1:
        for time in sorted(times):
            print(time)
    elif opc == 2:
        busca = input('Qual time deseja procurar? ')
        if busca in times:
            print(f'O {busca} está na {times.index(busca) + 1}ª posição.')
        else:
            print('Time não encontrado na lista.')
    elif opc == 3:
        for i, t in enumerate(times[:5], 1):
            print(f'{i}º {t}')
    elif opc == 4:
        for i, t in enumerate(times[-4:], 17):
            print(f'{i}º {t}')
    elif opc == 5:
        print('Saindo... Até a próxima!')
        break
    else:
        print('Opção inválida!')