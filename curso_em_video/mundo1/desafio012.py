preço = float(input("Qual o valor do produto? "))
n = preço - (preço * 5 / 100)

print("O preço do produto com 5% de desconto é de R${:.2f}".format(n))
