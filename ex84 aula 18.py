dados = []
grupo = []
maior = menor = 0
while True:
    dados.append((str(input('Nome: '))).strip())
    dados.append((float(input('Peso: '))))
    if len(grupo) == 0:   # logo apois receber dados verifica quem tem maior peso e menor peso
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    grupo.append(dados[:])  # faz a copia de dados
    dados.clear()  # deleta dados ( obrigatorio )
    r = str(input('Quer Continuar: [S/N]')).strip().upper()[0]
    if r in 'N':
        break
print('-='* 30)
print(f'Ao todo, cadrastrou {len(grupo)} pessoas.')
print(f'O maior peso foi {maior}Kg que foi de : ', end='')
for p in grupo:
    if p[1] == maior:  # fazer um laço para adicionar nome das pessoas com maior peso
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi {menor}Kg que foi de : ', end='')
for p in grupo:
    if p[1] == menor:  # fazer laço para adicionar nome das pessoas com menor peso
        print(f'[{p[0]}] ', end='')