import os

# Lista 

Lista_compras = []

# Estrutura

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela para melhor visualização
    print("\n==== LISTA DE COMPRAS ====") #Menu inicial
    print("")
    opcao = input("Escolha uma opção: [i]nserir, [a]pagar, [l]istar ou [s]air: ").lower()

    if opcao == 'i': 
        item = input("Digite o item a ser adicionado: ").strip()
        if item:
            Lista_compras.append(item)
            print(f"'{item}' adicionado à lista!")
        else:
            print("Item vazio! Por favor, digite um nome válido.")
            continue

    elif opcao == 'a':
        if not Lista_compras:
            print("A lista está vazia! Não há itens para apagar.")
        else: 
             print("\n Itens na lista de compras:")
        for i, item in enumerate(Lista_compras, start=1):
                print(f"{i}. {item}")
        try:
                indice = int(input("Digite o número do item a ser apagado: "))
                if 1 <= indice <= len(Lista_compras):
                    item_removido = Lista_compras.pop(indice - 1)
                    print(f"'{item_removido}' removido da lista!")
                else:
                    print("Número inválido! Por favor, escolha um número válido.")
        except ValueError:
                print("Entrada inválida! Por favor, digite um número.")

    elif opcao == 'l':
        if not Lista_compras:
            print("A lista está vazia!")
        else:
            print("\n Itens na lista de compras:")
            for i, item in enumerate(Lista_compras, start=1):
                print(f"{i}. {item}")
                continue

    elif opcao == 's':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")