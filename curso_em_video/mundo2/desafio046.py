from time import sleep

print('Contagem regressiva para o estouro do fogos de artifício!')
sleep(1)

for count in range(10, -1, -1):
    print(count)
    sleep(1)

print('BUM! BUM! POOOW!')