num = input("Digite um numero: ")

a = num - 1 
b = num + 1

print('Analizando o valor {}, seu antecessor é {} e seu sucessor é {},'.format(num, a, b))
## ou
print('Analizando o valor {}, seu antecessor é {} e seu sucessor é {},'.format(num, (num-1), (num+1)))
