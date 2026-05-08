from datetime import date

ano_atual = date.today().year

ano = int(input('Informe o ano de nascimento do atleta: '))

idade = ano_atual - ano

if idade <= 9:
    print(f'O atleta tem {idade} anos. Categoria: MIRIM.')
elif idade > 9 and idade <= 14:
    print(f'O atleta tem {idade} anos. Categoria: INFANTIL.')
elif idade > 14 and idade <= 19:
    print(f'O atleta tem {idade} anos. Categoria: JUNIOR.')
elif idade > 19 and idade <= 25:
    print(f'O atleta tem {idade} anos. Categoria: SÊNIOR.')
else:
    print(f'O atleta tem {idade} anos. Categoria: MASTER.')