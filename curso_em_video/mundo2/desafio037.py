n = int(input('Digite um número: '))
print('''Escolha uam das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')

opção = int(input('Sua opção: '))

if opção == 1:
    print(f'{n} convertido para binário é igual a {bin(n)[2:]}')
elif opção == 2:
    print(f'{n} convertido para octal é igual a {oct(n)[2:]}')
elif opção == 3:
    print(f'{n} convertido para hexadecimal é igual a {hex(n)[2:]}')
else:    
    print('Opção inválida!')
