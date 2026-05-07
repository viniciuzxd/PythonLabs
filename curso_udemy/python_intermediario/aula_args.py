### Multiplicar argumentos

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

resultado_multiplicacao = multiplicar(1, 2, 3, 4, 5)
print(f"O resultado da multiplicação é: {resultado_multiplicacao}")

### par ou impar

def par_ou_impar(numero):
    if numero % 2 == 0:
        return f'{numero} é Par'
    return f'{numero} é Ímpar'

resultado_par_impar = par_ou_impar(9)
print(resultado_par_impar)


