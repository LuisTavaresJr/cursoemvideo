from random import randint
from time import sleep
tenta = 0
print('VOU PENSAR EM UM NÚMERO ENTRE 0 E 10 ! TENTE ADIVINHAR')
computador = randint(0, 10)
acertou = False
while not acertou:
    tenta += 1
    jogador = int(input('Qual seu palpite: '))
    print('PROCESSANDO...')
    sleep(1)
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez!')
        elif jogador > computador:
            print('Menos... Tente mais uma vez!')

print(f'Parabéns você acertou! Eu e você pensamos em {computador} !')
print(f'Você tentou {tenta} vezes!')