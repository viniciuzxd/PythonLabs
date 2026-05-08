name = str(input('Qual é o seu nome? ')).strip()

print('Seu nome em maiúsculas é {}.'.format(name.upper()))
print('Seu nome em minúsculas é {}.'.format(name.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(name) - name.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(name.find(' ')))
