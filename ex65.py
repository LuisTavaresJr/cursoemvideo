r = 'S'
soma = tenta = maior = menor = 0
while r in 'S':
    n = int(input('Digite um número: '))
    soma += n
    tenta += 1
    if tenta == 1:
         maior = n
         menor = n
    else:
        if  n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Quer continuar: [S/N]')).upper().strip()[0]
media = soma / tenta
print('~'*30)
print(f'A soma dos números foi {soma}.\nFoi digitado {tenta} números.\nA média entre eles são de {media:.2f}.')
print(f'Maior {maior} menor {menor}')
