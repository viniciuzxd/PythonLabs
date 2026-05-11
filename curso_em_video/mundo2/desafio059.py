n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('-=-=-=-=-=-=-=-=')
    print('''Escolha a opção desejada:
    [1] - soma
    [2] - multiplicação
    [3] - maior
    [4] - novos números
    [5] - sair do programa
    ''')
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é igual a {}.'.format(n1, n2, soma))
    elif opção == 2:
        multiplicação = n1 * n2
        print('A multiplicação entre {} e {} é igual a {}.'.format(n1, n2, multiplicação))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {}, o maior valor é {}.'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
print('Fim do programa! Volte sempre!')
