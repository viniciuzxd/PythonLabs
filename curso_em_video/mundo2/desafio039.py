from datetime import date

ano_atual = date.today().year
ano = int(input('Informe seu ano de nascimento: '))

idade = ano_atual - ano

if idade < 18:
    print(f'Quem nasceu em {ano} tem {idade} anos. Ainda faltam {18 - idade} anos para o alistamento.')
elif idade == 18:
    print(f'Quem nasceu em {ano} tem {idade} anos. Você deve se alistar IMEDIATAMENTE!')
else:
    print(f'Quem nasceu em {ano} tem {idade} anos. Você já deveria ter se alistado há {idade - 18} anos.')



