n = int(input('Digite um número para calcular seu Factorial: '))
f = 1
for i in range(n, 0, -1):
    print(f'{i}', end=' ')
    print('x ' if i > 1 else '= ', end='')
    f *= i
print(f'{f}', end='')