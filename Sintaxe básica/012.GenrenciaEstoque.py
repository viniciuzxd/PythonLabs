estoque = []

def adicionar_material(noome, preco):
    item = {
        "nome": noome,
        "preco": preco
    }
    estoque.append(item)
    print(f"✅ {noome} adicionado com sucesso!")

def listar_estoque():
    print("\n--- PRODUTOS EM ESTOQUE ---")
    for item in estoque:
        print(f"Nome: {item['nome']}, Preço: {item['preco']}")

# Estrutura de menu

while True:
    print("\n1. Cadastrar | 2. Listar | 3. Sair")
    opcao = input("Escolha: ")

    try:
        if opcao == '1':
            n = input("Nome do produto: ").strip()
            try:
                p = float(input("Preço: ").replace(",", "."))
                adicionar_material(n, p)
            except ValueError:
                print("❌ Erro: Preço inválido.")
        elif opcao == '2':
            listar_estoque()
        elif opcao == '3':
            break
    except ValueError:
        print("❌ Erro: Preço inválido.")