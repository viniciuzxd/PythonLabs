from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))

#Foi Guanabara, já avancei um pouco, mas não tinha visto o desafio 60, então fiz do meu jeito, sem usar a função pronta. O código ficou assim:
n = int(input('Digite um número para calcular seu Fatorial: '))
f = 1
for c in range(n, 0, -1):
    f *= c
print('O fatorial de {} é {}.'.format(n, f))