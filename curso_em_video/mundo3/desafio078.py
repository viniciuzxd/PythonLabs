numeros = []

for c in range(0, 5):
    num = int(input('Digite um valor  número: '))
    numeros.append(num)

print(f'Os valores digitados foram: {numeros}')
print(f'O maior valor digitado foi {max(numeros)} na posição {numeros.index(max(numeros)) + 1}')
print(f'O menor valor digitado foi {min(numeros)} na posição {numeros.index(min(numeros)) + 1}')