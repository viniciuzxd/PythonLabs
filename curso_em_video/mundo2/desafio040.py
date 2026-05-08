n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

print(f'A média entre {n1} e {n2} é igual a {media:.1f}')

if media < 5.0:
    print('REPROVADO!')
elif media >= 5.0 and media <= 6.9:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')