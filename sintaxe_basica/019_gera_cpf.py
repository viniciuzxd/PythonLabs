import random

# GERA OS 9 PRIMEIROS DÍGITOS
nove_digitos = ""
for i in range(9):
    nove_digitos += str(random.randint(0, 9))

cpf_base = nove_digitos

# 1º dígito
soma = 0
multiplicador = 10

for digito in cpf_base:
    soma += int(digito) * multiplicador
    multiplicador -= 1

validador1 = (soma * 10) % 11
digito_1 = validador1 if validador1 <= 9 else 0

# 2º dígito
dez_digitos = cpf_base + str(digito_1)

soma = 0
multiplicador = 11

for digito in dez_digitos:
    soma += int(digito) * multiplicador
    multiplicador -= 1

validador2 = (soma * 10) % 11
digito_2 = validador2 if validador2 <= 9 else 0

# MONTANDO O CPF COMPLETO (11 números)
cpf_gerado = cpf_base + str(digito_1) + str(digito_2)
cpf_formatado = f"{cpf_gerado[:3]}.{cpf_gerado[3:6]}.{cpf_gerado[6:9]}-{cpf_gerado[9:]}"

print(f"CPF Gerado com sucesso: {cpf_formatado}")