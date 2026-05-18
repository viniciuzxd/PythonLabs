aluno = {}

aluno['nome'] = str(input('Nome do aluno: ')).strip()
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['média'] >= 7.0:
    aluno['situação'] = 'Aprovado'
elif 5.0 <= aluno['média'] < 7.0:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print('-=' * 20)

for chave, valor in aluno.items():
    print(f'  - {chave.capitalize()} é igual a {valor}')