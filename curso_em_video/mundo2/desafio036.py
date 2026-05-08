# regra: a prestação não pode ser superior a 30% do salário

c = float(input('Qual o valor da casa? R$'))
s = float(input('Qual o salário do comprador? R$'))
a = int(input('Em quantos anos ele vai pagar? '))

prestação = c / (a * 12)

if prestação > (s * 0.3):
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado!')