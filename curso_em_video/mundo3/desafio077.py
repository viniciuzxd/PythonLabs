palavras_temp = []

for c in range(1, 6):
    palavra = input('Digite a {} palavra: '.format(c))
    palavras_temp.append(palavra)

palavras = tuple(palavras_temp)

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais:  ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')