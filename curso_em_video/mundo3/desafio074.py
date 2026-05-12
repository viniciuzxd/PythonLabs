from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), 
           randint(1, 10), randint(1, 10))
print('Os números sorteados foram: {}'.format(numeros), end='')
print('\nO maior número sorteado foi: {}'.format(max(numeros)))
print('O menor número sorteado foi: {}'.format(min(numeros)))