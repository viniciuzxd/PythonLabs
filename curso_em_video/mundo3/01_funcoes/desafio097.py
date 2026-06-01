# Definição da Função
def escreva(msg):
    # Calcula o tamanho da mensagem e adiciona um "respiro" de 4 espaços (2 de cada lado)
    tam = len(msg) + 4
    
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)

# Programa Principal testando tamanhos diferentes
escreva('Olá, Mundo!')
escreva('Iniciando ambiente Zorin OS...')
escreva('C#')