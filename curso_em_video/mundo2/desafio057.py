s = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]

while s not in 'MF':
    s = str(input('Dados inválidos. Por favor, digite o sexo [M/F]: '))
print('Sexo {} registrado com sucesso.'.format(s))