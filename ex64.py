cont = soma = n = 0
print('Para parar digite 999!')
n = int(input('Digite um número: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número: '))
print(f'Você digitou {cont} números e a soma deles foi {soma} .')