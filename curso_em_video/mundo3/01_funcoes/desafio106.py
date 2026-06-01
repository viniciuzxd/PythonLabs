# Tupla global com códigos ANSI para pintar o terminal
cores = ('\033[m',         # 0 - Sem cor
         '\033[0;30;41m',  # 1 - Vermelho
         '\033[0;30;42m',  # 2 - Verde
         '\033[0;30;43m',  # 3 - Amarelo
         '\033[0;30;44m',  # 4 - Azul
         '\033[7;40m'      # 5 - Branco (Invertido)
         )

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(cores[5], end='') # Muda fundo para branco
    help(com)
    print(cores[0], end='') # Reseta cor

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(cores[0], end='')

# Programa Principal (O loop do sistema)
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)