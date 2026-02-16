class Carrinho:
    def __init__(self):
        self.itens = []
        self.desconto_taxa = 0.1

    def adicionar_preco(self, valor):
        self.itens.append(valor)
        print(f"✅ R$ {valor:.2f} adicionado!")

    def exibir_resumo(self):
        print("\n--- RESUMO DO CARRINHO ---")
        if not self.itens:
            print("Carrinho vazio.")
            return

        for idx, preco in enumerate(self.itens, start=1):
            if preco > 100:
                final = preco * (1 - self.desconto_taxa)
                print(f"{idx}. R$ {final:.2f} (Desconto aplicado! Original: R$ {preco:.2f})")
            else:
                print(f"{idx}. R$ {preco:.2f}")

# O LOOP PRINCIPAL

meu_carrinho = Carrinho() # objeto

while True:
    produto = input("Valor do produto (ou 'sair' para encerrar, 'carrinho' para ver resumo): ").strip().replace(',', '.')
    
    if produto.lower() == 'sair':
        break
    else:
        if produto.lower() == 'carrinho':
            meu_carrinho.exibir_resumo()
            continue
    
    try:
        preco_limpo = float(produto)
        if preco_limpo < 0:
            print("❌ Erro: Valor negativo.")
            continue
            
        meu_carrinho.adicionar_preco(preco_limpo)

    except ValueError:
        print("⚠️ Digite um número válido.")

meu_carrinho.exibir_resumo()