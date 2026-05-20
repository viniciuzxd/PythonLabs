from time import sleep

def maior(* num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    
    maior_valor = 0
    tamanho = len(num)

    for contador, valor in enumerate(num):
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        
        if contador == 0 or valor > maior_valor:
            maior_valor = valor
            
    print(f'Foram informados {tamanho} valores ao todo.')
    
    if tamanho > 0:
        print(f'O maior valor informado foi {maior_valor}.')
    else:
        print('Nenhum valor foi informado para análise.')

# --- Programa Principal (Testando a Modularização) ---

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()