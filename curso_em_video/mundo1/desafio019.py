import random

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))

lista = [a1, a2, a3, a4]
escolha = random.choice(lista)
print('O aluno sorteado para apagar o quadro foi: {}'.format(escolha))

# Minha primeira solução, sem usar lista
# import random
# alunos = ['Suh', 'Lívia', 'Kássia', 'Leilane']
# print('O aluno sorteado para apagar o quadrofoi: {}'.format(random.choice(alunos)))