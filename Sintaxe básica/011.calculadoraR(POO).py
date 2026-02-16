class Calculadora:
    def somar(self, n1, n2): return n1 + n2
    def subtrair(self, n1, n2): return n1 - n2
    def multiplicar(self, n1, n2): return n1 * n2
    def dividir(self, n1, n2):
        if n2 == 0:
            raise ZeroDivisionError("Não dá para dividir por zero!")
        return n1 / n2
    def potencia(self, n1, n2): return n1 ** n2

# Instanciando a classe
calc = Calculadora()

print("=== CALCULADORA ROBUSTA ===")

while True:
    try:
        conta = input("\nDigite a conta (ex: 5 + 5) ou 'sair': ").lower().strip()
        
        if conta == 'sair':
            print("Desligando...")
            break

        partes = conta.split()
        
        if len(partes) != 3:
            print("⚠️ Digite no formato: numero operador numero (ex: 10 + 2)")
            continue

        num1 = float(partes[0].replace(",", "."))
        operador = partes[1]
        num2 = float(partes[2].replace(",", "."))

        # Lógica de escolha
        if operador == '+':
            resultado = calc.somar(num1, num2)
        elif operador == '-':
            resultado = calc.subtrair(num1, num2)
        elif operador == '*':
            resultado = calc.multiplicar(num1, num2)
        elif operador == '/':
            resultado = calc.dividir(num1, num2)
        elif operador == '**':
            resultado =calc.potencia(num1, num2)
        else:
            print("❌ Operador inválido! Use +, -, * ou /")
            continue

        print(f"📊 Resultado: {resultado}")

    except ZeroDivisionError as e:
        print(f"🛑 Erro: {e}")
    except ValueError:
        print("🛑 Erro: Digite apenas números válidos!")
    except Exception as e:
        print(f"🛑 Algo deu errado: {e}")