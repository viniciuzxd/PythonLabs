# set contidown
contador = 0

while contador <= 30:
    contador += 1

    if contador == 13:
        print('Sexta feira 13')
        continue

    if contador == 22:
        print('Dois patinhos na lagoa')
        continue

    print(contador)

    if contador == 25:
        print('End.')
        break

