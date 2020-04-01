print('Loja do NoMaike')
total = quant = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: ')).strip().upper()
    preco = float(input('Preço: R$'))
    total += preco
    cont += 1
    resp = ' '
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    if preco > 1000:
        quant += 1
    while resp not in 'SN':
        resp = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    if resp == 'N':
        break

print('{:-^40}'.format(' Fim do Programa '))
print(f'O total da compra foi R${total}')
print(f'Temos {quant} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa {menor:.2f}')
