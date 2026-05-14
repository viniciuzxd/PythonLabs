from random import randint
from time import sleep

lista_principal = []
dados_temporarios = []

print('-=' * 30)
print(f'{"JOGA NA MEGA SENA":^60}')
print('-=' * 30)

quant_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1

while total <= quant_jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        
        if num not in dados_temporarios:
            dados_temporarios.append(num)
            cont += 1
            
        if cont >= 6:
            break
            
    dados_temporarios.sort()
    
    lista_principal.append(dados_temporarios[:])
    
    dados_temporarios.clear()
    total += 1

print('-=' * 5, f' SORTEANDO {quant_jogos} JOGOS ', '-=' * 5)
for i, l in enumerate(lista_principal):
    print(f'Jogo {i+1}: {l}')
    sleep(1) 
    
print('-=' * 5, ' < BOA SORTE! > ', '-=' * 5)