soma = 0
contador = 0

while True:
    n = int(input('Digite um número inteiro (999 para parar): '))
    
    if n == 999:
        break
    
    soma += n
    contador += 1
    
print('Foram digitados {} números e a soma entre eles é {}.'.format(contador, soma))