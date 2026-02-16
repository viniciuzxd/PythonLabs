#For por baixo dos panos 
#Lista = iterador
lista = [1, 2, 3, 4, 5] #Sem o iter, a lista é apenas uma coleção de itens, não é um iterador.
num = iter(lista)

while True:
    try:
        item = next(num)
        print(item)
    except StopIteration:
        print("Fim da lista.")
        break

#Usando o for normalmente

for item in lista:
    print(item)