sal = float(input("Qual é o salário do funcionário? "))

novo = sal + (sal * 15 / 100)

print("O funcionário que ganhava R${:.2f}, com 15% de aumento, passará a ganhar R${:.2f}.".format(sal, novo))