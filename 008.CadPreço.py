# Lista
precos_validos = []

# Desconto
desconto = 0.1  # 10% de desconto

print("=== cadastro de preços ===")

# estrutura
while True:
    produto = input("Informe o valor do produto (ou Digite 'sair' para encerrar o cadastro ou 'carrinho' para ver os preços cadastrados): ").strip().replace(',', '.')

    if produto == 'Sair' or produto == 'sair':
        break
    elif produto == 'Carrinho' or produto == 'carrinho':
        print("\n--- RESUMO DO CARRINHO ---")
        for idx, preco in enumerate(precos_validos, start=1):
            if preco > 100:
                # Calcula o valor final com desconto
                preco_final = preco * (1 - desconto)
                print(f"{idx}. R$ {preco_final:.2f} (Desconto de 10% aplicado! Valor original: R$ {preco:.2f})")
            else:
                # Se for 100 ou menos, apenas exibe o preço normal
                print(f"{idx}. R$ {preco:.2f}")
        continue

    try:
        preco = float(produto)
        if preco <= 0:
            print("Valor inválido! O preço deve ser maior que zero.")
            continue
        precos_validos.append(preco)
        print(f"✅ R$ {preco:.2f} adicionado!")

    except ValueError:
        print("Valor inválido! Digite apenas números ou 'sair' para encerrar.")
        continue

# Exibir os preços cadastrados
print("\n--- RESUMO DO CARRINHO ---")

for idx, preco in enumerate(precos_validos, start=1):
    if preco > 100:
        # Calcula o valor final com desconto
        preco_final = preco * (1 - desconto)
        print(f"{idx}. R$ {preco_final:.2f} (Desconto de 10% aplicado! Valor original: R$ {preco:.2f})")
    else:
        # Se for 100 ou menos, apenas exibe o preço normal
        print(f"{idx}. R$ {preco:.2f}")