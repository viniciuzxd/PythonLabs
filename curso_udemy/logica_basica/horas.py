entrada_hora = input("Que horas são? (Digite apenas o número de 0 a 23): ")

try:
    hora = int(entrada_hora)

    if 0 <= hora <= 11:
        print("Bom dia!")
    elif 12 <= hora <= 17:
        print("Boa tarde!")
    elif 18 <= hora <= 23:
        print("Boa noite!")
    else:
        print("Hora inválida. Por favor, digite um número entre 0 e 23.")
except ValueError:
    print("Por favor, digite apenas números inteiros.")