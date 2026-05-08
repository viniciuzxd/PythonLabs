soma = 0
count = 0

for n in range(1, 7):
    num = int(input('Digite o {} número: '.format(n)))
    if num % 2 == 0:
        soma += num
        count += 1
print('Você informou {} números pares é {}.'.format(count, soma))

