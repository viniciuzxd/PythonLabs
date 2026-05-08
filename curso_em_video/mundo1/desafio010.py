# considerando que USS1,00 = R$3,27

real = float(input("Quanto dinheiro tens na carteira? ")).replace(',' '.')

dol = real / 3.27

print("Com {} reais, você pode comprar US${}.".format(real, dol)) 