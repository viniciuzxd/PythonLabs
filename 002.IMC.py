#Obter dados do usuário
Nome = input("Digite seu nome: ")
Peso = float(input("Digite seu peso em kg: "))
Altura = float(input("Digite sua altura em metros: "))

#Calcular IMC
IMC = Peso / (Altura ** 2)

#Classificar IMC
if IMC < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= IMC < 24.9:
    classificacao = "Peso normal"
elif 25 <= IMC < 29.9:
    classificacao = "Sobrepeso"
elif 30 <= IMC:
    classificacao = "Obesidade"

#Exibir resultado
print(f"{Nome}, seu IMC é {IMC:.2f}, o que indica que você está classificado como: {classificacao}.")
