quant = soma = 0
print('Digite 999 pra parar o programa!')
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    quant += 1
    soma += n
print(f'Você digitou {quant} números e a soma deles foi {soma}.')
