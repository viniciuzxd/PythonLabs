pilha = []

print('-=' * 30)
print('''menu:
      [1] vailidar expressão:
      [2] sair''')

expressao = str(input('Digite a expressão matemática: '))

if expressao == '1':
    for caractere in expressao:
        if caractere == '(':
            pilha.append('(') 
            
        elif caractere == ')':
            if len(pilha) > 0:
                pilha.pop() 
            else:
                pilha.append(')') 
                break

if len(pilha) == 0:
    print('Sua expressão está válida! Todos os parênteses fecharam.')
else:
    print('Sua expressão está errada! Verifique os parênteses.')