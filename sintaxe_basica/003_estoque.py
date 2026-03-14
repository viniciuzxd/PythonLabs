try:
    # Dados do produto
    Produto = input("Digite o nome do produto: ")
    Estoque = int(input("Digite a quantidade em estoque: "))
    Valor = float(input("Digite o valor do produto: "))

    # Valor em estoque do produto
    Valor_Estoque = Estoque * Valor

    # Verificar valor em estoque (Lógica de classificação)
    if Valor_Estoque > 1000:
        classificacao = "Estoque de Alto Valor"
    elif 500 <= Valor_Estoque <= 1000:
        classificacao = "Estoque de Médio Valor"
    else:
        classificacao = "Estoque de Baixo Valor"

    print(f"\nO valor total em estoque de {Produto.upper()} é R${Valor_Estoque:.2f}.")
    print(f"Classificação: {classificacao}")

except ValueError:
    print("\n[ERRO] Valor inválido! No estoque use números inteiros e no valor use apenas números e ponto.")