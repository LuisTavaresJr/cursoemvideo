peso = float(input('Qual é seu peso: [Kg]'))
altura = float(input('Qual é sua altura: [m]'))
imc = peso / (altura ** 2)
print(f'O seu IMC é de {imc:.2f}.')
if imc < 18.5:
    print(f'Você está Abaixo do peso normal.')
elif 18.5 <= imc < 25:
    print('Você esta no peso IDEAL.')
elif 25 <= imc < 30:
    print('você esta em SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE.')
else:
    print('Você está em OBESIDADE MÓRBIDA.')