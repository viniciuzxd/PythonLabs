import os

# 1. Configuração inicial
segredo = input("Digite a palavra secreta: ").strip().lower()
tentativas = 5
letras_acertadas = [] 
letras_erradas = [] # <-- NOVA LISTA

while tentativas > 0:
    # Limpa a tela no início de cada rodada
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("\n" + "="*20)
    print(f"Tentativas restantes: {tentativas}")
    print(f"Letras que você já errou: {', '.join(letras_erradas)}") # <-- EXIBE OS ERROS
    print("="*20)
    
    # 2. Desenha a palavra na tela
    palavra_exibida = ""
    for letra in segredo:
        if letra in letras_acertadas:
            palavra_exibida += letra + " "
        else:
            palavra_exibida += "_ "
    
    print(f"\nPalavra: {palavra_exibida}")
    
    # 3. Verifica vitória
    if "_" not in palavra_exibida:
        print("\n🎉 Parabéns! Você venceu!")
        break

    # 4. Entrada do usuário
    tentativa = input("\nTente uma letra (ou a palavra inteira): ").strip().lower()

    # Atalho de vitória
    if tentativa == segredo:
        print("\n🎉 MESTRE! Você adivinhou a palavra inteira!")
        break

    # Validação de repetição
    if tentativa in letras_acertadas or tentativa in letras_erradas:
        print(f"⚠️ Você já tentou '{tentativa}'! Tente outra.")
        input("Pressione Enter para continuar...") # Pausa para o usuário ler
        continue

    # 5. Lógica de Acerto ou Erro
    if tentativa in segredo:
        print(f"✅ Boa! A letra '{tentativa}' existe.")
        letras_acertadas.append(tentativa)
    else:
        tentativas -= 1
        letras_erradas.append(tentativa) # <-- GUARDA O ERRO
        print(f"❌ Errou! '{tentativa}' não está na palavra.")
    
    input("Pressione Enter para continuar...") # Pausa para o usuário ler

# 6. Fim de jogo
if tentativas == 0:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n💀 Game Over! A palavra era: {segredo}")