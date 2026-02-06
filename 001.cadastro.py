from datetime import date

# Obtendo o ano atual automaticamente
ano_atual = date.today().year

# Coletando os dados
nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite seu ano de nascimento: "))
altura = float(input("Digite sua altura em metros: "))

# Calculando a idade
idade = ano_atual - ano_nascimento

# Verificando a maioridade
if idade >= 18:
    status_maioridade = "maior de idade"
else:
    status_maioridade = "menor de idade"

# Retornando a resposta completa
print("\n--- Resumo do Perfil ---")
print(f"Olá {nome}! Você nasceu em {ano_nascimento} e tem {idade} anos.")
print(f"Sua altura é de {altura}m e você é {status_maioridade}.")