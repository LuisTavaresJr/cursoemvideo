print('Dizer se o número é primo!')
n = int(input('Digite um número: '))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        print(f'\033[33m', end='')
        cont += 1
    else:
        print('\033[31m', end= '')
    print(f'{c} ', end='')
if cont == 2:
    print(f'\n\033[mO número {n} foi divisivel {cont} vezes. Entao ele é PRIMO')
else:
    print(f'\n\033[mO número {n}, foi divisivel {cont} vezes. Então ele NÃO é PRIMO')