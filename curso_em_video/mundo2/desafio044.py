v = float(input('Informe o valor do produto: R$'.replace(',', '.')))
p = int(input('''forme a forma de pagamento:
[1] à vista dinheiro
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Sua opção: '''))

if p == 1:
    print(f'O valor total é de R${v * 0.9:.2f}')
elif p == 2:
    print(f'O valor total é de R${v * 0.95:.2f}')
elif p == 3:
    print(f'O valor total é de R${v:.2f}')
else:
    print(f'O valor total é de R${v * 1.2:.2f}')