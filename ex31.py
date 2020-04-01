print('Viagem de onibus, vamos calcular o valor da passagem!')
viagem = int(input('Digite a distancia da sua viagem: '))
if viagem <= 200:
    passagem = viagem * 0.50
    print(f'Sua passagem ficou no valor de R${passagem}')
else:
    passagem = viagem * 0.45
    print(f'Sua passagem ficou no valor de R${passagem}')
print('Obrigado !')