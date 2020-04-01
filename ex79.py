valores = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valores: # se n nao estiver em valores
        valores.append(n)
        print('Valor Adicionado com sucesso!')
    else:
        print('Número duplicado, não vou adicionar')
    resp = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Os valores digitados foi {sorted(valores)}')
