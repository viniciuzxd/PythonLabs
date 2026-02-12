estoque = []

def adicionar_produto(nome, preco):
    item = {
        "nome": nome, 
        "preco": preco
    }
    estoque.append(item)
    print(f"✅ {nome} adicionado com sucesso!")

def listar_estoque():
    print("\n--- PRODUTOS EM ESTOQUE ---")
    if not estoque:
        print("Estoque vazio.")
    else:
        for produto in estoque:
            print(f"📦 Nome: {produto['nome']} | 💰 Preço: R$ {produto['preco']:.2f}")

# --- Menu Principal ---
while True:
    print("\n1. Cadastrar | 2. Listar | 3. Sair")
    opcao = input("Escolha: ")

    if opcao == '1':
        n = input("Nome do produto: ").strip()
        try:
            p = float(input("Preço: ").replace(",", "."))
            adicionar_produto(n, p)
        except ValueError:
            print("❌ Erro: Preço inválido.")
            
    elif opcao == '2':
        listar_estoque()
        
    elif opcao == '3':
        break
    else:
        print("Opção inválida.")