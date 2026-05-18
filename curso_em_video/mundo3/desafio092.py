from datetime import datetime

dados = {}

dados['nome'] = str(input('Nome: ')).strip()
nascimento = int(input('Ano de Nascimento: '))

ano_atual = datetime.now().year
dados['idade'] = ano_atual - nascimento

dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    
    anos_de_contribuicao = 35
    ano_aposentadoria = dados['contratação'] + anos_de_contribuicao
    dados['aposentadoria'] = dados['idade'] + (ano_aposentadoria - ano_atual)

print('-=' * 20)

for chave, valor in dados.items():
    if chave == 'salário':
        print(f'  - {chave} tem o valor R$ {valor:.2f}')
    else:
        print(f'  - {chave} tem o valor {valor}')