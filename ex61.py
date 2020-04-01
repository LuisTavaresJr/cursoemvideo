print('Gerador de PA')
primeiro = int(input('Digite um número para mostrar a PA: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('ACABOU !')