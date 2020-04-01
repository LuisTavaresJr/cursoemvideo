ficha = []
while True:
    nome = str(input('Nome: ')).strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media]) # adicionando na lista ja criando listas
    resp = str(input('Quer continuar: [S/N]')).upper().strip()[0]
    if resp in "N":
        break
print('=-'* 30)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
print('-'* 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
while True:
    print('Digite [999] para sair!')
    opc = int(input('De qual aluno quer ver as notas: '))
    print('-'* 30)
    if opc == 999:
        print('Interropendo...')
        break
    if opc <= len(ficha)- 1:
        print(f'As notas de {ficha[opc][0]} foi {ficha[opc][1]}')
        print('-'* 30)
print('Volte Sempre!')