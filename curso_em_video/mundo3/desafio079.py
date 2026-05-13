
number = []

while True:
    print('-=' * 30)
    print('''Menu:
    [1] Adicionar número
    [2] Mostrar números na ordem crescente
    [3] Sair''')
    print('-=' * 30)

    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        while True:
            num = int(input('Digite um número: '))
            if num not in number:
                number.append(num)
                print('Número adicionado com sucesso!')
            else:
                print('Número repetido. Não vou adicionar.')
            
            continuar = input('Quer adicionar mais algum? [S/N] ').upper().strip()
            if continuar == 'N':
                break 

    elif opcao == 2:
        if len(number) == 0:
            print('A lista está vazia. Adicione números primeiro.')
        else:
            number.sort()
            print(f'Os números em ordem crescente são: {number}')
    elif opcao == 3:
        print('Saindo do programa. Até mais!')
        break
