nome = input("Digite seu primeiro nome: ")
tamanho = len(nome)

if tamanho > 1: # Verifica se algo foi digitado
    if tamanho <= 4:
        print("Seu nome é curto.")
    elif 5 <= tamanho <= 6:
        print("Seu nome é normal.")
    else:
        print("Seu nome é muito grande.")
else:
    print("Por favor, digite pelo menos uma letra.")