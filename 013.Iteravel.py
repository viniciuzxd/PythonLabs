#For por baixo dos panos 
#Lista = iterador
lista = [1, 2, 3, 4, 5] #Sem o iter, a lista é apenas uma coleção de itens, não é um iterador.
num = iter(lista)

while True:
    try:
        item = next(num)
        print(item)
    except StopIteration:
        print("Fim da lista.")
        break

#Usando o for normalmente

for item in lista:
    print(item)

# Complicando

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
            p = float(input("Preço: ").replace(",", "."))
            adicionar_material(n, p)
        elif opcao == '2':
            listar_estoque()
        elif opcao == '3':
            break
    except ValueError:
        print("❌ Erro: Preço inválido.")