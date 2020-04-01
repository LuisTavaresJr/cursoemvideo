from time import sleep
print('Contagem Regressiva !')
n = int(input('Qual o tempo (Em Segundos) da contagem regressiva: '))
for c in range(n, -1, -1):
    print(c)
    sleep(1)
print('Feliz Ano Novo!')