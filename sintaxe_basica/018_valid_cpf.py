# validador de CPF 
cpf_usuario = input("Insira seu CPF: ")
cpf_limpo = cpf_usuario.replace('.', '').replace('-', '').strip()

if len(cpf_limpo) != 11:
    print("Erro: O CPF precisa ter 11 números.")

else: 
    # 1 digito
    soma = 0
    multiplicador = 10

    for digito in cpf_limpo[:9]:
        soma += int(digito) * multiplicador
        multiplicador -= 1

    validador1 = (soma * 10) % 11
    digito_1 = validador1 if validador1 <= 9 else 0

    # 2 digito
    dez_digitos = cpf_limpo[:9] + str(digito_1)

    soma = 0
    multiplicador = 11

    for digito in dez_digitos:
        soma += int(digito) * multiplicador
        multiplicador -= 1

    validador2 = (soma * 10) % 11
    digito_2 = validador2 if validador2 <= 9 else 0

# validando o cpf
    cpf_calculado = cpf_limpo[:9] + str(digito_1) + str(digito_2)
    if cpf_calculado == cpf_limpo:
        print("CPF válido!")
    else:
        print("CPF inválido!")