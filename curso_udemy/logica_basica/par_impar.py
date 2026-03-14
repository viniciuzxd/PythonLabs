entrada = input("Digite um número inteiro: ")

if entrada.isdigit():
    numero = int(entrada)
    if numero % 2 == 0:
        print(f"O número {numero} é PAR.")
    else:
        print(f"O número {numero} é ÍMPAR.")
else:
    print("Isso não é um número inteiro.")