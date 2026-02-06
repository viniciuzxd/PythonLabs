# Set senha e tentativas
senha = "labpython2024"
tentativas = 3

print("=== Sistema de Acesso ===")

# estrutura
while tentativas > 0:
    try: 
        entrada = input('Digite sua senha de acesso: ')
        if entrada == senha:
            print("Acesso concebido!")
            break
        else:
            tentativas -= 1
            print(f"Senha incorreta! Tentativas restantes: {tentativas}")
            continue
    except Exception as e:
        print(f"Erro inesperado: {e}")
        continue

if tentativas == 0:
    print("Acesso negado! Número de tentativas esgotadas.")
