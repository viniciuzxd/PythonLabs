total = 0

print("--- SISTEMA DE ORÇAMENTO ---")

while True:
    produto = input("\nNome do produto (ou 'fim' para encerrar): ").strip()

    # Lógica do BREAK
    if produto.lower() == 'fim':
        break
    
    # Lógica do CONTINUE (Se o nome estiver vazio)
    if not produto:
        print("Erro: Nome do produto não pode ser vazio!")
        continue

    # Lógica do TRATAMENTO + SOMA
    try:
        preco = float(input(f"Preço de {produto}: R$ "))
        total += preco
        print(f"Subtotal: R$ {total:.2f}")
    except ValueError:
        print("Preço inválido! Digite apenas números.")
        continue

print(f"\n✅ Orçamento Finalizado! Total: R$ {total:.2f}")