dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))

preço = (dias * 60) + (km * 0.15)

print('O preço a pagar é de R${:.2f}'.format(preço))