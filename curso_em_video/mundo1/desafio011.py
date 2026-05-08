v = float(input("Largura da Parede: "))
h = float(input("Altura da Parede: "))

a = v * h 
tinta = a / 2

print("A área da parede é de {}m²".format(a))
print("A quantidade de tinta necessária para pintar a parede é de {} litros".format(tinta))