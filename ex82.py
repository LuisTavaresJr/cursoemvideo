valores = []
impar = []
par = []
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    r = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    if r in 'N':
        break
print('-='* 30)
print(f'A lista foi {valores}')
print(f'A lista de números PARES: {par}')
print(f'A lista de números ÍMPARES: {impar}')
