from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Sua opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO !')
print('-='* 11)
print(f'O computador jogou {itens[computador]}')
print(f'Você jogou {itens[jogador]}')
print('-='* 11)
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('Jogo EMPATOU!')
    elif jogador == 1:
        print('Jogador Ganhou!')
    elif jogador == 2:
        print('Computador Ganhou!')
    else:
        print('Opção Invalida!')

elif computador == 1: #computador jogou pepal
    if jogador == 0:
        print('Computador Ganhou!')
    elif jogador == 1:
        print('Jogo EMPATOU!')
    elif jogador == 2:
        print('Jogador Ganhou!')
    else:
        print('Opção Invalida!')
elif computador == 2:# computador jogou tesoura
    if jogador == 0:
        print('Jogador Ganhou!')
    elif jogador == 1:
        print('Computador Ganhou!')
    elif jogador == 2:
        print('Jogo EMPATOU!')
    else:
        print('Opção Invalida!')
