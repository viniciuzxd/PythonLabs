from random import randint

print('🤖 Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

computador = randint(0, 10)
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1 # O contador ganha +1 a cada tentativa
    
    if jogador == computador:
        acertou = True 
    else:
        
        if jogador < computador:
            print('⬆️ Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('⬇️ Menos... Tente mais uma vez.')

print('\n🎉 ACERTOU! Você platinou o jogo com {} tentativas.'.format(palpites))