
def analisar_texto(texto):
    palavras = texto.split()
    vogais = "aeiouAEIOU"
    
    total_vogais = sum(1 for letra in texto if letra in vogais)
    total_consoantes = sum(1 for letra in texto if letra.isalpha() and letra not in vogais)
    maior_palavra = max(palavras, key=len) if palavras else ""
    frase_invertida = " ".join(palavra[::-1] for palavra in palavras)

    dados = {
        "total_vogais": total_vogais,
        "total_consoantes": total_consoantes,
        "total_palavras": len(palavras),
        "maior_palavra": maior_palavra,
        "maior_palavra_invertida": maior_palavra[::-1],
        "frase_invertida": frase_invertida
    }

    return dados

# Exemplo de uso

resultado = analisar_texto("Olá, mundo! Este é um teste.")

print(f"Total de vogais: {resultado['total_vogais']}")
print(f"Total de consoantes: {resultado['total_consoantes']}")
print(f"Total de palavras: {resultado['total_palavras']}")
print(f"A maior palavra é: {resultado['maior_palavra']}")
print(f"A maior palavra invertida é: {resultado['maior_palavra_invertida']}")
print(f"Frase invertida: {resultado['frase_invertida']}")