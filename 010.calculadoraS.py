# menu
print("=== CALCULADORA SIMPLES ===")
print("Dica: Digite a conta com espaços (ex: 10 + 2)")

# entrada do usuário
while True:
    conta = input("Digite a conta (ou 'sair' para encerrar): ").strip().lower()
    if conta == "sair":
        print("Encerrando a calculadora. Até mais!")
        break
    elif conta == "":
        print("Entrada vazia. Por favor, digite uma conta válida.")
        continue

    try:
        itens = conta.split() 

        if len(itens) != 3:
            print("⚠️ Erro: Use espaços entre os números e o operador.")
            continue
        
        num1 = float(itens[0].replace(",", "."))  
        operador = itens[1]
        num2 = float(itens[2].replace(",", "."))

        if operador == "+":
            resultado = num1 + num2
        elif operador == "-":
            resultado = num1 - num2
        elif operador == "*":
            resultado = num1 * num2
        elif operador == "/":
            if num2 != 0:
                resultado = num1 / num2
            else:
                print("Erro: Divisão por zero não é permitida.")
                continue
        else:
            print("Operador inválido. Use +, -, *, ou /.")
            continue

        print(f"Resultado: {resultado:.2f}")

    except ValueError:
        print("Erro: Certifique-se de que os números estão corretos e use o formato adequado.")