nume_list_temp = []

while True:
    print('-=' * 30)
    print('''Menu:
    [1] Adicionar número
    [2] Mostrar todos números em ordem
    [3] Mostrar listas com números pares e ímpares
    [4] Sair''')

    op = int(input('Escolha uma opção: '))

    if op == 1:
        while True:
            num = int(input('Digite um número: '))
            nume_list_temp.append(num)
            
            while cont not in 'SN':
                cont = input('Inválido. Quer adicionar mais algum? [S/N] ').upper().strip()
            if cont == 'N':
                break

    elif op == 2:
        if len(nume_list_temp) == 0:
            print('A lista está vazia. Adicione números primeiro.')
        else:
            print(f'Os números em ordem são: {sorted(nume_list_temp)}')

    elif op == 3:
        if len(nume_list_temp) == 0:
            print('A lista está vazia. Adicione números primeiro.')
        else:
            pares = [num for num in nume_list_temp if num % 2 == 0]
            impares = [num for num in nume_list_temp if num % 2 != 0]
            print(f'Lista de números pares: {pares}')
            print(f'Lista de números ímpares: {impares}')

    elif op == 4:
        print('Saindo do programa. Até mais!')
        break