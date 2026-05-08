primeiro = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
decimo = primeiro + (10 - 1) * razão

for c in range(primeiro, decimo, razão):
    print('{} '.format(c), end='→ ')
print('ACABOU!')