soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma += n
        cont += 1
print(f'''A soma de todos os números múltiplos de 3 entre 1 e 500 é {soma}''')
print(f'''A quantidade de números múltiplos de 3 entre 1 e 500 é {cont}''')