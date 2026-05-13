number = []

while True:
    print('-=' * 30)
    print('''Menu:
    [1] Adicionar números
    [2] Mostrar números em ordem
    [3] Sair''')

    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        for c in range(0, 5):
            num = int(input('Digite um número: '))
            
            if len(number) == 0 or num > number[-1]:
                number.append(num)
                print('Número adicionado com sucesso!')
            else:
                pos = 0
                while pos < len(number):
                    if num <= number[pos]:
                        number.insert(pos, num)
                        print('Número adicionado com sucesso!')
                        break
                    pos += 1
                    
    elif opcao == 2:
        print(f'Os números em ordem: {number}')
        
    elif opcao == 3:
        print('Saindo do programa. Até mais!')
        break