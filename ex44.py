print('Lojas NoMaike!')
compras = float(input('Qual o valor das compras: R$'))
print('''Qual a forma de pagamento:
[1] Á vista 10% de desconto
[2] Á vista no cartão 5% de desconto
[3] 2x no cartão, sem desconto
[4] 3x no cartão ou mais 20% de juros''')
opcao = int(input('Qual opção: '))
if opcao == 1:
    pagar = compras - (compras * 10/100)
    print(f'Sua compra de R${compras:.2f}, á vista você pagará R${pagar:.2f}.')
elif opcao == 2:
    pagar = compras - (compras * 5/100)
    print(f'Sua compra de R${compras:.2f}, você pagará R${pagar:.2f}.')
elif opcao == 3:
    parcelas = compras / 2
    print(f'Sua compra vai ter 2 parcelas de R${parcelas:.2f} cada.')
elif opcao == 4:
    parcelas = int(input('Quantas parcelas: '))
    pagar = (compras + (compras * 20/100)) / parcelas
    print(f'Sua compra vai ter {parcelas} parcelas no valor de R${pagar:.2f} cada.')
else:
    print('Opcão Errada, Tente novamente!')
