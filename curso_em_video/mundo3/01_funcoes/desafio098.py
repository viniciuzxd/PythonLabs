from time import sleep

# Definição da Função
def contador(inicio, fim, passo):
    # Tratamento de Erros (Edge Cases)
    if passo < 0:
        passo *= -1 # Transforma número negativo em positivo
    if passo == 0:
        passo = 1   # Impede loop infinito se o usuário digitar passo 0

    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1.5)

    # Lógica de contagem crescente
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont += passo
        print('FIM!')
        
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont -= passo
        print('FIM!')

# --- Programa Principal ---

contador(1, 10, 1)

contador(10, 0, 2)

print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
f = int(input('Fim:    '))
pas = int(input('Passo:  '))

contador(ini, f, pas)