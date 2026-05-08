from random import randint

print('=-=' * 20)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10. Você consegue adivinhar qual é?')
print('=-=' * 20)

num = randint(0, 10)

palpite = int(input('Qual é o seu palpite? '))

if palpite == num:
    print('Parabéns! Você acertou!')
else:
    print('Que pena! Você errou. O número era {}.'.format(num))