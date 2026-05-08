p = float(input('Informe seu peso (kg): '))
h = float(input('Informe sua altura (m): '))

imc = p / (h ** 2)

print(f'Seu IMC é de {imc:.1f}')

if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif imc >= 18.5 and imc < 25:
    print('Você está com o PESO IDEAL!')
elif imc >= 25 and imc < 30:
    print('Você está com SOBREPESO!')
elif imc >= 30 and imc < 40:
    print('Você está com OBESIDADE!')
else:
    print('Você está com OBESIDADE MÓRBIDA!')