from random import randint
from time import sleep
print('VOU PENSAR EM UM NÚMERO ENTRE 0 E 5 ! TENTE ADIVINHAR')
jogador = int(input('Digite um número entre 0 e 5: '))
computador = randint(0, 5)
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print(f'Parabéns você Venceu! Eu e você pensamos em {computador} !')
else:
    print(f'Ganhei! Pensei em {computador} e você em {jogador}')
print('fim')