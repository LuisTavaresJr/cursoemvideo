print('Gerador de PA')
primeiro = int(input('Digite um número para mostrar a PA: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA. !')
    mais = int(input('Quantos termos você quer mostrar mais? :'))
print('Fim!')
