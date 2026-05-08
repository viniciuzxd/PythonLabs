name = str(input('Digite seu nome completo: ')).strip()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(name.split()[0]))
print('Seu último nome é {}'.format(name.split()[-1]))