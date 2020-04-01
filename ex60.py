n = int(input('Digite um número para calcular seu Factorial: '))
f = 1
c = n
print(f'Calculando o Factorial de {n}! ', end='')
while c > 0:
    print(f'{c}', end=' ')
    print('x 'if c > 1 else '=', end='')
    f *= c
    c -= 1
print(f' {f}')