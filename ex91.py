from random import randint
from time import sleep
from operator import itemgetter # fuciona para ordenar os dicionarios
jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}
rank = {}
print('Valores sortedos')
for k, v in jogo.items(): # como é dicionario tem que usar .items()
    print(f'{k} tirou {v} no dado.')
    sleep(1)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True) # coloca em ordem pela parte (1), que é os valores do dado.
print('-='* 30)
for i, v in enumerate(rank): # como rank é uma lista tem que usar o enumerate
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
