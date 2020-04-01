from time import sleep
print('Limite maximo 80km/h !')
carro = float(input('Qual a velocidade do carro: '))
sleep(1)
if carro > 80:
    multa = (carro - 80) * 7
    print(f'Você ultrapassou o limite de velocidade.\nVocê recebeu uma multa de R${multa:.2f}!')
print('Boa viagem! Digija com segurança!')