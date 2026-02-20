# Lista
vogais = ['a', 'e', 'i', 'o', 'u']
totalVogais = 0
consonantes = 0

# Pede a frase au usuario
frase = input("Digite uma frase: ").lower()
palavras = frase.split()

#Estrutura

for letra in frase:
    if letra in vogais:
        totalVogais += 1
    elif letra.isalpha():
        consonantes += 1

# Maior palavra
maior_palavra = ""
for palavra in palavras:
    if len(palavra) > len(maior_palavra):
        maior_palavra = palavra

# 3. Inverter as palavras (mantendo a ordem)
frase_invertida = ""
for palavra in palavras:
    palavra_invertida = ""
    # Inverte as letras da palavra atual
    for letra in palavra:
        palavra_invertida = letra + palavra_invertida 
    
    # Adiciona a palavra invertida na frase final 
    frase_invertida = frase_invertida + palavra_invertida + " "

# Exibe os resultados gerais 

print(f"Total de vogais: {totalVogais}" + f"\nTotal de consoantes: {consonantes}")
print(f"Total de palavras: {len(palavras)}")
print(f"A maior palavra é: {maior_palavra}")
print(f"A maior palavra invertida é: {maior_palavra[::-1]}")
print(f"Frase invertida: {frase_invertida.strip()}")