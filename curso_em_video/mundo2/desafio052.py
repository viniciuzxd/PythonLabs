num = int(input('Digite um número inteiro: '))

tot_divisores = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ') # Código ANSI para Amarelo (é divisor)
        tot_divisores += 1
    else:
        print('\033[31m', end=' ') # Código ANSI para Vermelho (não é divisor)
    
    print('{}'.format(c), end=' ')

print('\033[m') 
print('\nO número {} foi divisível {} vezes.'.format(num, tot_divisores))

if tot_divisores == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')