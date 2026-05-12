palavras_temp = []

for c in range(1, 6):
    palavra = input('Digite a {} palavra: '.format(c))
    palavras_temp.append(palavra)

palavras = tuple(palavras_temp)

for p in palavras:
    print('Na palavra {} temos as vogais:  '.format(p.upper()))
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')