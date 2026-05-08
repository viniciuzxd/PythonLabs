# cobrar R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.

d = float(input('Digite a distância da viagem em km: '))

if d <=200:
    p = d * 0.50 
    print(f'O preço da viagem é R$ {p:.2f}')
else:
    p = d * 0.45
    print(f'O preço da viagem é R$ {p:.2f}')