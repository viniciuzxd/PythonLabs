ficha = []

# FASE 1: Coleta e Processamento de Dados
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    
    ficha.append([nome, [nota1, nota2], media])
    
    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    while resp not in 'SN':
        resp = input('Opção inválida. Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break

print('-=' * 30)

print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)

for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

print('-=' * 30)

while True:
    busca = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    
    if busca == 999:
        print('FINALIZANDO O SISTEMA...')
        break
    
    if busca <= len(ficha) - 1 and busca >= 0:
        print(f'As notas de {ficha[busca][0]} são {ficha[busca][1]}')
    else:
        print('Aluno não encontrado. Tente novamente.')
        
print('<<< VOLTE SEMPRE >>>')