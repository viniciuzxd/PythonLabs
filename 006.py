# Exercicio comentado
# --- FUNÇÕES (Nossas ferramentas) ---

def limpar_valor(texto):
    """Transforma '1.500,00' em float 1500.0"""
    return float(texto.replace(".", "").replace(",", "."))

def calcular_salario_liquido(bruto):
    """Aplica um desconto fixo de 10% de impostos"""
    return bruto * 0.90

def exibir_colaborador(nome, salario):
    """Formata a exibição do resultado"""
    print(f"\n👤 Colaborador: {nome}")
    print(f"💰 Salário Líquido: R$ {salario:.2f}")
    print("-" * 20)

# --- LOOP PRINCIPAL (Onde o programa acontece) ---

print("=== SISTEMA DE RH 1.0 ===")

while True:
    nome = input("\nNome do colaborador (ou 'sair'): ").strip()
    
    if nome.lower() == 'sair':
        break
    
    salario_bruto_texto = input(f"Digite o salário bruto de {nome}: ").strip()

    try:
        # Aqui usamos nossas funções como peças de Lego
        valor_numerico = limpar_valor(salario_bruto_texto)
        valor_final = calcular_salario_liquido(valor_numerico)
        
        # Chamamos a função de exibição
        exibir_colaborador(nome, valor_final)

    except ValueError:
        print("❌ Erro: Por favor, digite um valor salarial válido.")

print("\nSistema encerrado.")